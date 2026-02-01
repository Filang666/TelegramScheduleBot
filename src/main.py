import asyncio

from aiogram_run import BotApplication

if __name__ == "__main__":
    app = BotApplication()

    # Parse schedule (optional)
    # app.parse_schedule()

    # Run bot
    asyncio.run(app.main())
