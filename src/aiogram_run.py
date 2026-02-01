import asyncio

import parsing
from create_bot import bot, dp
from handlers.start import start_router


async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # parsing.parse_url(parsing.url_list)
    # parsing.download_files(parsing.url_list)
    asyncio.run(main())
