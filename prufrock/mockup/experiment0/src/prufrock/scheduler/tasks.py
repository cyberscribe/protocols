import logging
import uuid
from datetime import datetime, time, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from sqlalchemy import select
from zoneinfo import ZoneInfo

from prufrock.config import settings
from prufrock.db.models import Experiment, Prompt, Response
from prufrock.db.session import db_session
from prufrock.protocol.arc import (
    build_antithesis,
    get_open_prompt,
    is_complete,
)
from prufrock.scheduler.fire_window import random_fire_time

logger = logging.getLogger(__name__)

DAILY_RESEED_JOB_ID = "daily_reseed"


async def fire_prompt(bot, experiment_id: str, day_number: int) -> None:
    exp_uuid = uuid.UUID(experiment_id)
    with db_session() as session:
        experiment = session.get(Experiment, exp_uuid)
        if experiment is None or experiment.status != "active":
            logger.warning("fire_prompt: experiment %s not active; skipping.", experiment_id)
            return

        prompt = get_open_prompt(session, experiment)
        if prompt is None:
            logger.info("fire_prompt: no open prompt for experiment %s; may be complete.", experiment_id)
            return

        # Day might have shifted if a previous firing was missed
        if prompt.day_number != day_number:
            logger.info(
                "fire_prompt: scheduled day %d but open day is %d; firing open day.",
                day_number,
                prompt.day_number,
            )

        a, b = prompt.antithesis_a, prompt.antithesis_b
        chat_id = experiment.participant.telegram_chat_id
        message_text = f"Day {prompt.day_number} of 14.\n\n{a}\n{b}\n\nContinue."

        msg = await bot.send_message(chat_id=chat_id, text=message_text)
        prompt.fired_at = datetime.now(timezone.utc)
        prompt.telegram_message_id = msg.message_id

    logger.info("Fired prompt day %d for experiment %s.", prompt.day_number, experiment_id)


def _get_or_create_next_prompt(session, experiment: Experiment) -> Prompt | None:
    """Return the open prompt for this experiment, creating it if it doesn't yet exist."""
    if is_complete(session, experiment):
        return None

    open_prompt = get_open_prompt(session, experiment)
    if open_prompt is not None:
        return open_prompt

    # Determine the next day number from answered prompts
    answered_days = (
        session.execute(
            select(Prompt.day_number)
            .join(Response, Response.prompt_id == Prompt.id)
            .where(Prompt.experiment_id == experiment.id)
        )
        .scalars()
        .all()
    )
    next_day = (max(answered_days) + 1) if answered_days else 1

    if next_day > 14:
        return None

    a, b = build_antithesis(session, experiment, next_day)
    prompt = Prompt(
        id=uuid.uuid4(),
        experiment_id=experiment.id,
        day_number=next_day,
        antithesis_a=a,
        antithesis_b=b,
        scheduled_for=datetime.now(timezone.utc),
    )
    session.add(prompt)
    session.flush()
    return prompt


async def daily_reseed(bot, scheduler: AsyncIOScheduler) -> None:
    """Book today's fire time for every active experiment."""
    tz = ZoneInfo(settings.timezone)
    waking_start = time.fromisoformat(settings.waking_start_local)
    waking_end = time.fromisoformat(settings.waking_end_local)

    with db_session() as session:
        active_experiments = (
            session.execute(select(Experiment).where(Experiment.status == "active"))
            .scalars()
            .all()
        )

        for experiment in active_experiments:
            prompt = _get_or_create_next_prompt(session, experiment)
            if prompt is None:
                continue

            job_id = f"fire_{experiment.id}_{prompt.day_number}"
            if scheduler.get_job(job_id):
                logger.debug("Job %s already scheduled; skipping.", job_id)
                continue

            fire_at = random_fire_time(waking_start, waking_end, tz)
            scheduler.add_job(
                fire_prompt,
                trigger=DateTrigger(run_date=fire_at),
                args=[bot, str(experiment.id), prompt.day_number],
                id=job_id,
                replace_existing=True,
            )
            logger.info(
                "Scheduled fire for experiment %s day %d at %s.",
                experiment.id,
                prompt.day_number,
                fire_at.isoformat(),
            )


def schedule_daily_reseed(scheduler: AsyncIOScheduler, bot) -> None:
    tz = ZoneInfo(settings.timezone)
    scheduler.add_job(
        daily_reseed,
        "cron",
        hour=0,
        minute=1,
        timezone=tz,
        args=[bot, scheduler],
        id=DAILY_RESEED_JOB_ID,
        replace_existing=True,
    )
    logger.info("Daily reseed job registered at 00:01 %s.", settings.timezone)
