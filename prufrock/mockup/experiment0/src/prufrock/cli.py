import json
import logging
import uuid as _uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated

import typer
from sqlalchemy import select

from prufrock.config import settings

app = typer.Typer(help="Prufrock experiment 0 — operator CLI.", add_completion=False)
logger = logging.getLogger(__name__)


def _logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )


# ── seed-sonnets ──────────────────────────────────────────────────────────────

@app.command("seed-sonnets")
def seed_sonnets(
    json_path: Annotated[
        Path, typer.Argument(help="Path to shakespeare_sonnets.json")
    ],
    regenerate: Annotated[
        bool,
        typer.Option(
            "--regenerate",
            help="Fetch from Gutenberg and regenerate the JSON before loading.",
        ),
    ] = False,
) -> None:
    """Load sonnets from JSON into the sonnets table (idempotent)."""
    _logging(settings.log_level)
    from prufrock.protocol.voltas import (
        fetch_gutenberg_text,
        load_sonnets_json,
        parse_sonnets,
        save_sonnets_json,
    )
    from prufrock.db.models import Sonnet
    from prufrock.db.session import db_session

    if regenerate or not json_path.exists():
        typer.echo("Fetching sonnets from Gutenberg…")
        raw = fetch_gutenberg_text()
        sonnets = parse_sonnets(raw)
        save_sonnets_json(sonnets, json_path)
        typer.echo(f"Saved {len(sonnets)} records to {json_path}.")
    else:
        sonnets = load_sonnets_json(json_path)
        typer.echo(f"Loaded {len(sonnets)} records from {json_path}.")

    with db_session() as session:
        inserted = skipped = excluded = 0
        for s in sonnets:
            if s["excluded"]:
                excluded += 1
                continue
            if session.get(Sonnet, s["id"]) is not None:
                skipped += 1
                continue
            session.add(
                Sonnet(
                    id=s["id"],
                    title=s["title"],
                    source=s["source"],
                    full_text=s["full_text"],
                    line_12=s["line_12"],
                    line_13=s["line_13"],
                )
            )
            inserted += 1

    typer.echo(
        f"Inserted {inserted} sonnets; {skipped} already present; {excluded} excluded (sonnet 126)."
    )


# ── register-participant ──────────────────────────────────────────────────────

@app.command("register-participant")
def register_participant(
    telegram_user_id: Annotated[
        int, typer.Option("--telegram-user-id", help="Numeric Telegram user ID")
    ],
    telegram_chat_id: Annotated[
        int,
        typer.Option(
            "--telegram-chat-id",
            help="Numeric Telegram chat ID (same as user ID for personal bots)",
        ),
    ],
    display_name: Annotated[str, typer.Option("--display-name")] = "Robert",
    tz: Annotated[str, typer.Option("--timezone")] = "",
) -> None:
    """Register a participant (idempotent)."""
    _logging(settings.log_level)
    from prufrock.db.models import Participant
    from prufrock.db.session import db_session

    effective_tz = tz or settings.timezone

    with db_session() as session:
        existing = session.execute(
            select(Participant).where(Participant.telegram_user_id == telegram_user_id)
        ).scalar_one_or_none()

        if existing is not None:
            typer.echo(f"Participant {telegram_user_id} already registered (id={existing.id}).")
            return

        participant = Participant(
            telegram_user_id=telegram_user_id,
            telegram_chat_id=telegram_chat_id,
            display_name=display_name,
            timezone=effective_tz,
        )
        session.add(participant)
        session.flush()
        typer.echo(f"Registered participant '{display_name}' (id={participant.id}).")


# ── start-experiment ──────────────────────────────────────────────────────────

@app.command("start-experiment")
def start_experiment(
    participant_telegram_id: Annotated[
        int,
        typer.Option(
            "--participant-telegram-id",
            help="Defaults to TELEGRAM_USER_ID from .env",
        ),
    ] = 0,
) -> None:
    """Start a new 14-day experiment for the registered participant."""
    _logging(settings.log_level)
    from prufrock.db.models import Experiment, Participant, Sonnet
    from prufrock.db.session import db_session
    from prufrock.protocol.arc import start_experiment as arc_start

    uid = participant_telegram_id or settings.telegram_user_id

    with db_session() as session:
        participant = session.execute(
            select(Participant).where(Participant.telegram_user_id == uid)
        ).scalar_one_or_none()
        if participant is None:
            typer.echo(
                f"No participant found for telegram_user_id={uid}. "
                "Run register-participant first.",
                err=True,
            )
            raise typer.Exit(1)

        active = session.execute(
            select(Experiment)
            .where(Experiment.participant_id == participant.id)
            .where(Experiment.status == "active")
        ).scalar_one_or_none()
        if active is not None:
            typer.echo(
                f"Participant already has an active experiment ({active.id}). "
                "Run abandon-experiment first.",
                err=True,
            )
            raise typer.Exit(1)

        experiment = arc_start(session, participant)
        sonnet = session.get(Sonnet, experiment.sonnet_id)
        assert sonnet is not None

    typer.echo(f"Experiment {experiment.id} started.")
    typer.echo(f"Sonnet {experiment.sonnet_id}:")
    typer.echo(f"  S₁: {sonnet.line_12}")
    typer.echo(f"  S₂: {sonnet.line_13}")
    typer.echo("The bot will fire its first prompt at a random time in today's waking-hours window.")


# ── status ────────────────────────────────────────────────────────────────────

@app.command("status")
def status(
    participant_telegram_id: Annotated[
        int,
        typer.Option(
            "--participant-telegram-id",
            help="Defaults to TELEGRAM_USER_ID from .env",
        ),
    ] = 0,
) -> None:
    """Print the current experiment state and assembled poem."""
    _logging(settings.log_level)
    from prufrock.db.models import Experiment, Participant
    from prufrock.db.session import db_session
    from prufrock.protocol.arc import get_poem_state

    uid = participant_telegram_id or settings.telegram_user_id

    with db_session() as session:
        participant = session.execute(
            select(Participant).where(Participant.telegram_user_id == uid)
        ).scalar_one_or_none()
        if participant is None:
            typer.echo(f"No participant found for telegram_user_id={uid}.")
            raise typer.Exit(1)

        experiment = session.execute(
            select(Experiment)
            .where(Experiment.participant_id == participant.id)
            .where(Experiment.status == "active")
        ).scalar_one_or_none()
        if experiment is None:
            typer.echo("No active experiment.")
            return

        lines = get_poem_state(session, experiment.id)
        responses_so_far = max(0, len(lines) - 2)

        typer.echo(f"Experiment : {experiment.id}")
        typer.echo(f"Sonnet     : {experiment.sonnet_id}")
        typer.echo(f"Day        : {responses_so_far + 1} of 14 ({responses_so_far} responses recorded)")
        typer.echo(f"Status     : {experiment.status}")
        typer.echo("")
        typer.echo("Poem so far:")
        for i, line in enumerate(lines):
            label = f"S{i+1}" if i < 2 else f"R{i-1}"
            typer.echo(f"  [{label}] {line}")


# ── abandon-experiment ────────────────────────────────────────────────────────

@app.command("abandon-experiment")
def abandon_experiment(
    participant_telegram_id: Annotated[
        int,
        typer.Option(
            "--participant-telegram-id",
            help="Defaults to TELEGRAM_USER_ID from .env",
        ),
    ] = 0,
) -> None:
    """Mark the active experiment as abandoned."""
    _logging(settings.log_level)
    from prufrock.db.models import Experiment, Participant
    from prufrock.db.session import db_session

    uid = participant_telegram_id or settings.telegram_user_id

    with db_session() as session:
        participant = session.execute(
            select(Participant).where(Participant.telegram_user_id == uid)
        ).scalar_one_or_none()
        if participant is None:
            typer.echo("No such participant.", err=True)
            raise typer.Exit(1)

        experiment = session.execute(
            select(Experiment)
            .where(Experiment.participant_id == participant.id)
            .where(Experiment.status == "active")
        ).scalar_one_or_none()
        if experiment is None:
            typer.echo("No active experiment to abandon.")
            return

        experiment.status = "abandoned"
        experiment.completed_at = datetime.now(timezone.utc)

    typer.echo(f"Experiment {experiment.id} marked as abandoned.")


# ── fire-now ──────────────────────────────────────────────────────────────────

@app.command("fire-now")
def fire_now(
    participant_telegram_id: Annotated[
        int,
        typer.Option(
            "--participant-telegram-id",
            help="Defaults to TELEGRAM_USER_ID from .env",
        ),
    ] = 0,
) -> None:
    """Immediately fire today's prompt (smoke-test helper)."""
    _logging(settings.log_level)
    import asyncio
    from telegram import Bot
    from prufrock.db.models import Experiment, Participant
    from prufrock.db.session import db_session
    from prufrock.scheduler.tasks import _get_or_create_next_prompt

    uid = participant_telegram_id or settings.telegram_user_id

    async def _fire() -> None:
        bot = Bot(token=settings.telegram_bot_token)
        async with bot:
            with db_session() as session:
                participant = session.execute(
                    select(Participant).where(Participant.telegram_user_id == uid)
                ).scalar_one_or_none()
                if participant is None:
                    typer.echo("No participant found.", err=True)
                    return

                experiment = session.execute(
                    select(Experiment)
                    .where(Experiment.participant_id == participant.id)
                    .where(Experiment.status == "active")
                ).scalar_one_or_none()
                if experiment is None:
                    typer.echo("No active experiment.", err=True)
                    return

                prompt = _get_or_create_next_prompt(session, experiment)
                if prompt is None:
                    typer.echo("Experiment complete — nothing to fire.")
                    return

                a, b = prompt.antithesis_a, prompt.antithesis_b
                msg_text = f"Day {prompt.day_number} of 14.\n\n{a}\n{b}\n\nContinue."
                msg = await bot.send_message(
                    chat_id=participant.telegram_chat_id, text=msg_text
                )
                prompt.fired_at = datetime.now(timezone.utc)
                prompt.telegram_message_id = msg.message_id

        typer.echo(f"Fired day {prompt.day_number} prompt.")

    asyncio.run(_fire())


# ── export ────────────────────────────────────────────────────────────────────

@app.command("export")
def export(
    experiment_id: Annotated[
        str, typer.Option("--experiment-id", help="UUID of the experiment to export")
    ],
) -> None:
    """Dump an experiment to JSON (stdout) for archival."""
    _logging(settings.log_level)
    from prufrock.db.models import Experiment, Prompt
    from prufrock.db.session import db_session

    exp_uuid = _uuid.UUID(experiment_id)

    with db_session() as session:
        experiment = session.get(Experiment, exp_uuid)
        if experiment is None:
            typer.echo(f"Experiment {experiment_id} not found.", err=True)
            raise typer.Exit(1)

        prompts = (
            session.execute(
                select(Prompt)
                .where(Prompt.experiment_id == exp_uuid)
                .order_by(Prompt.day_number)
            )
            .scalars()
            .all()
        )

        data = {
            "experiment_id": str(experiment.id),
            "participant_id": str(experiment.participant_id),
            "sonnet_id": experiment.sonnet_id,
            "status": experiment.status,
            "started_at": experiment.started_at.isoformat() if experiment.started_at else None,
            "completed_at": (
                experiment.completed_at.isoformat() if experiment.completed_at else None
            ),
            "prompts": [
                {
                    "day_number": p.day_number,
                    "antithesis_a": p.antithesis_a,
                    "antithesis_b": p.antithesis_b,
                    "scheduled_for": p.scheduled_for.isoformat(),
                    "fired_at": p.fired_at.isoformat() if p.fired_at else None,
                    "response": (
                        {
                            "text": p.response.text,
                            "received_at": p.response.received_at.isoformat(),
                            "parent_hash_a": p.response.parent_hash_a,
                            "parent_hash_b": p.response.parent_hash_b,
                        }
                        if p.response
                        else None
                    ),
                }
                for p in prompts
            ],
        }

    typer.echo(json.dumps(data, indent=2))


if __name__ == "__main__":
    app()
