import asyncio
import logging
import os
import sys

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from create_bot import bot_handler
from handlers.start import StartHandler, start_router
from parsing import ScheduleParser


class BotApplication:
    def __init__(self):
        self.bot_handler = bot_handler
        self.schedule_parser = ScheduleParser()
        self.start_handler = StartHandler(start_router)
        self.logger = logging.getLogger(__name__)

    async def main(self) -> None:
        """Main application entry point."""
        self.logger.info("Starting bot application...")

        # Include routers
        self.bot_handler.dp.include_router(start_router)

        # Delete webhook and start polling
        await self.bot_handler.bot.delete_webhook(drop_pending_updates=True)
        self.logger.info("Bot started. Press Ctrl+C to stop.")
        await self.bot_handler.dp.start_polling(self.bot_handler.bot)

    def parse_schedule(self):
        """Parse and download schedule files."""
        try:
            self.logger.info("Starting schedule parsing...")
            urls = self.schedule_parser.parse_and_download()
            self.logger.info(
                f"Schedule parsing completed! Downloaded {len(urls)} files."
            )
            return urls
        except Exception as e:
            self.logger.error(f"Error during parsing: {e}")
            return []


async def main():
    """Main async entry point."""
    app = BotApplication()
    await app.main()


if __name__ == "__main__":
    # Create application instance
    app = BotApplication()

    # Uncomment to parse schedule on startup
    # app.parse_schedule()

    # Run the bot
    try:
        asyncio.run(app.main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
