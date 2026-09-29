import logging

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from db import init_db
import handlers


# =========================
# LOGGING
# =========================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# =========================
# STARTUP
# =========================

async def post_init(application: Application) -> None:
    """Bot ishga tushganda database tayyorlanadi."""
    init_db()
    logger.info("Database initialized successfully.")
    logger.info("Bot started successfully.")


# =========================
# ERROR HANDLER
# =========================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Botdagi xatolarni logga yozadi."""
    logger.exception(
        "Exception while handling an update:",
        exc_info=context.error,
    )


# =========================
# MAIN
# =========================

def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN topilmadi. .env faylga BOT_TOKEN kiriting."
        )

    # Telegram bot application
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # =========================
    # COMMAND HANDLERS
    # =========================

    application.add_handler(
        CommandHandler("start", handlers.start_command)
    )

    application.add_handler(
        CommandHandler("profile", handlers.profile_command)
    )

    application.add_handler(
        CommandHandler("balance", handlers.balance_command)
    )

    application.add_handler(
        CommandHandler("daily", handlers.daily_command)
    )

    application.add_handler(
        CommandHandler("help", handlers.help_command)
    )

    # =========================
    # MAFIA GAME
    # =========================

    application.add_handler(
        CommandHandler("game", handlers.game_command)
    )

    application.add_handler(
        CommandHandler("startgame", handlers.startgame_command)
    )

    application.add_handler(
        CommandHandler("players", handlers.players_command)
    )

    # =========================
    # ECONOMY
    # =========================

    application.add_handler(
        CommandHandler("send", handlers.send_command)
    )

    application.add_handler(
        CommandHandler("diamond", handlers.diamond_command)
    )

    # =========================
    # PARA
    # =========================

    application.add_handler(
        CommandHandler("para", handlers.para_command)
    )

    application.add_handler(
        CommandHandler("acceptpara", handlers.accept_para_command)
    )

    application.add_handler(
        CommandHandler("divorce", handlers.divorce_command)
    )

    # =========================
    # ADMIN
    # =========================

    application.add_handler(
        CommandHandler("admin", handlers.admin_command)
    )

    # =========================
    # INLINE BUTTONS
    # =========================

    application.add_handler(
        CallbackQueryHandler(handlers.callback_handler)
    )

    # =========================
    # ERROR HANDLER
    # =========================

    application.add_error_handler(error_handler)

    # =========================
    # START BOT
    # =========================

    logger.info("Starting Telegram polling...")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
