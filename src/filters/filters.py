from aiogram.filters import Filter
from aiogram.types import Message

from create_bot import BotHandler

# Create a BotHandler instance to access admins
bot_handler = BotHandler()
admins = bot_handler.admins


class AdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in admins


class NotAdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id not in admins
