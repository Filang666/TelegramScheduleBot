import os
import sys

from aiogram.filters import Filter
from aiogram.types import Message

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from create_bot import admins


class AdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in admins


class NotAdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id not in admins
