import logging
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters

from prufrock.bot.handlers import handle_reply, start
from prufrock.config import settings
from prufrock.scheduler.tasks import daily_reseed, schedule_daily_reseed

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)-8s %(name)s  %(message)s",
    )
    # Quiet down noisy libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("apscheduler").setLevel(logging.INFO)


def build_application() -> Application:
    tz = ZoneInfo(settings.timezone)
    scheduler = AsyncIOScheduler(timezone=tz)

    async def post_init(app: Application) -> None:
        schedule_daily_reseed(scheduler, app.bot)
        scheduler.start()
        logger.info("APScheduler started.")
        # Immediately seed today's fire time rather than waiting for 00:01
        await daily_reseed(app.bot, scheduler)

    async def post_shutdown(app: Application) -> None:
        if scheduler.running:
            scheduler.shutdown(wait=False)
        logger.info("APScheduler stopped.")

    app = (
        ApplicationBuilder()
        .token(settings.telegram_bot_token)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))
    return app


def main() -> None:
    setup_logging()
    logger.info("Starting Prufrock bot (long-poll mode).")
    app = build_application()
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
