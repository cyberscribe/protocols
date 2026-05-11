import logging

from sqlalchemy import select
from telegram import Update
from telegram.ext import ContextTypes

from prufrock.config import settings
from prufrock.db.models import Experiment, Participant
from prufrock.db.session import db_session
from prufrock.protocol.arc import (
    assemble_poem,
    get_open_prompt,
    is_complete,
    mark_complete,
    record_response,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user is None or update.message is None:
        return

    user_id = update.effective_user.id
    chat_id = update.effective_chat.id if update.effective_chat else user_id

    if user_id != settings.telegram_user_id:
        await update.message.reply_text("This is a private experiment bot.")
        return

    with db_session() as session:
        existing = session.execute(
            select(Participant).where(Participant.telegram_user_id == user_id)
        ).scalar_one_or_none()

        if existing is None:
            participant = Participant(
                telegram_user_id=user_id,
                telegram_chat_id=chat_id,
                display_name=update.effective_user.full_name,
                timezone=settings.timezone,
            )
            session.add(participant)
            session.flush()
            await update.message.reply_text(
                "Registered. Run `prufrock start-experiment` on the server to begin."
            )
            logger.info("Registered participant %d via /start.", user_id)
        else:
            await update.message.reply_text("Registered. Waiting for the next prompt.")


async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user is None or update.message is None or update.message.text is None:
        return

    user_id = update.effective_user.id
    if user_id != settings.telegram_user_id:
        return

    raw_text = update.message.text
    # Capture the first non-blank line; discard the rest (permissive, per §1.5)
    first_line = next((ln.strip() for ln in raw_text.splitlines() if ln.strip()), None)
    if not first_line:
        return

    raw_update = update.to_dict()

    with db_session() as session:
        participant = session.execute(
            select(Participant).where(Participant.telegram_user_id == user_id)
        ).scalar_one_or_none()

        if participant is None:
            await update.message.reply_text("Not registered. Send /start first.")
            return

        experiment = session.execute(
            select(Experiment)
            .where(Experiment.participant_id == participant.id)
            .where(Experiment.status == "active")
        ).scalar_one_or_none()

        if experiment is None:
            await update.message.reply_text("No active experiment at the moment.")
            return

        prompt = get_open_prompt(session, experiment)
        if prompt is None:
            await update.message.reply_text("No open prompt right now — sit tight.")
            return

        record_response(session, prompt, first_line, raw_update)

        if is_complete(session, experiment):
            mark_complete(session, experiment)
            poem = assemble_poem(session, experiment)
            await update.message.reply_text(f"The poem is complete.\n\n{poem}")
            logger.info("Experiment %s complete; poem delivered.", experiment.id)
        # Silent accept — no acknowledgement message, per the protocol's negative-space intent
