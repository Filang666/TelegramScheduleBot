import asyncio
import logging

from create_bot import BotHandler
from handlers.start import StartHandler, start_router
from parsing import ScheduleParser


class BotApplication:
    def __init__(self):
        self.bot_handler = BotHandler()
        self.schedule_parser = ScheduleParser()
        self.start_handler = StartHandler(self.bot_handler.admins, start_router)

    async def main(self) -> None:
        """Main application entry point."""
        # Include routers
        self.bot_handler.dp.include_router(start_router)

        # Delete webhook and start polling
        await self.bot_handler.bot.delete_webhook(drop_pending_updates=True)
        await self.bot_handler.dp.start_polling(self.bot_handler.bot)

    def parse_schedule(self) -> None:
        """Parse and download schedule files."""
        try:
            print("Starting schedule parsing...")
            self.schedule_parser.parse_and_download()
            print("Schedule parsing completed!")
        except Exception as e:
            print(f"Error during parsing: {e}")


if __name__ == "__main__":
    # Create application instance
    app = BotApplication()

    # Uncomment to parse schedule on startup
    # app.parse_schedule()

    # Run the bot
    asyncio.run(app.main())
