import hashlib
import logging
import secrets
import uuid
from datetime import datetime, timezone

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from prufrock.db.models import Experiment, Participant, Prompt, Response, Sonnet

logger = logging.getLogger(__name__)

TOTAL_DAYS = 14
EXCLUDED_SONNET_ID = 126

_rng = secrets.SystemRandom()


def _sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def start_experiment(session: Session, participant: Participant) -> Experiment:
    used_ids = (
        session.execute(
            select(Experiment.sonnet_id).where(
                Experiment.participant_id == participant.id
            )
        )
        .scalars()
        .all()
    )
    excluded = {EXCLUDED_SONNET_ID, *used_ids}

    fresh_ids = (
        session.execute(select(Sonnet.id).where(Sonnet.id.notin_(excluded)))
        .scalars()
        .all()
    )

    if not fresh_ids:
        # All 153 eligible sonnets exhausted; wrap to the full pool (minus 126)
        logger.info(
            "Participant %s has used all sonnets; wrapping to full pool.", participant.id
        )
        fresh_ids = (
            session.execute(
                select(Sonnet.id).where(Sonnet.id != EXCLUDED_SONNET_ID)
            )
            .scalars()
            .all()
        )

    chosen_id = _rng.choice(fresh_ids)
    sonnet = session.get(Sonnet, chosen_id)
    assert sonnet is not None, f"Sonnet {chosen_id} not found in DB"

    experiment = Experiment(
        id=uuid.uuid4(),
        participant_id=participant.id,
        sonnet_id=chosen_id,
        status="active",
        started_at=datetime.now(timezone.utc),
    )
    session.add(experiment)
    session.flush()
    logger.info(
        "Started experiment %s (sonnet %d) for participant %s.",
        experiment.id,
        sonnet.id,
        participant.id,
    )
    return experiment


def get_poem_state(session: Session, experiment_id: uuid.UUID) -> list[str]:
    """Return the ordered list of lines in the poem so far: [S₁, S₂, R₁, …]."""
    row = session.execute(
        text("SELECT lines FROM poem_state WHERE experiment_id = :eid"),
        {"eid": experiment_id},
    ).one_or_none()

    if row is None or row[0] is None:
        # Fallback for before any prompts exist (or if view returns null)
        experiment = session.get(Experiment, experiment_id)
        assert experiment is not None
        sonnet = session.get(Sonnet, experiment.sonnet_id)
        assert sonnet is not None
        return [sonnet.line_12, sonnet.line_13]

    return list(row[0])


def build_antithesis(
    session: Session, experiment: Experiment, day_number: int
) -> tuple[str, str]:
    """Return (P[N-1], P[N]) — the two lines preceding day N's synthesis."""
    lines = get_poem_state(session, experiment.id)
    # Day N needs indices N-1 and N (0-based); requires at least N+1 lines.
    if len(lines) < day_number + 1:
        raise ValueError(
            f"poem_state has {len(lines)} lines but day {day_number} needs at least "
            f"{day_number + 1}. Has R{day_number - 2} been recorded?"
        )
    return lines[day_number - 1], lines[day_number]


def get_open_prompt(session: Session, experiment: Experiment) -> Prompt | None:
    """The earliest prompt for this experiment that has no response yet."""
    answered_prompt_ids = select(Response.prompt_id)
    return session.execute(
        select(Prompt)
        .where(Prompt.experiment_id == experiment.id)
        .where(Prompt.id.notin_(answered_prompt_ids))
        .order_by(Prompt.day_number)
        .limit(1)
    ).scalar_one_or_none()


def record_response(
    session: Session,
    prompt: Prompt,
    line_text: str,
    raw_update: dict,
) -> Response:
    response = Response(
        id=uuid.uuid4(),
        prompt_id=prompt.id,
        text=line_text,
        parent_hash_a=_sha256(prompt.antithesis_a),
        parent_hash_b=_sha256(prompt.antithesis_b),
        received_at=datetime.now(timezone.utc),
        raw_update_json=raw_update,
    )
    session.add(response)
    session.flush()
    logger.info(
        "Recorded R%d for experiment %s: %r",
        prompt.day_number,
        prompt.experiment_id,
        line_text,
    )
    return response


def is_complete(session: Session, experiment: Experiment) -> bool:
    count = (
        session.execute(
            select(Response)
            .join(Prompt, Response.prompt_id == Prompt.id)
            .where(Prompt.experiment_id == experiment.id)
        )
        .scalars()
        .all()
    )
    return len(count) >= TOTAL_DAYS


def assemble_poem(session: Session, experiment: Experiment) -> str:
    lines = get_poem_state(session, experiment.id)
    return "\n".join(lines)


def mark_complete(session: Session, experiment: Experiment) -> None:
    experiment.status = "completed"
    experiment.completed_at = datetime.now(timezone.utc)
    session.flush()
    logger.info("Experiment %s marked complete.", experiment.id)
