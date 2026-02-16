import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram import Bot, Dispatcher
from aiogram.types import Update, Message, Chat, User

@pytest.fixture
def mock_bot():
    """Return a mocked Bot instance."""
    bot = AsyncMock(spec=Bot)
    bot.send_message = AsyncMock()
    bot.send_photo = AsyncMock()
    # Add other methods you use
    return bot

@pytest.fixture
def mock_message():
    """Return a mocked Message with basic attributes."""
    message = AsyncMock(spec=Message)
    message.chat = MagicMock(spec=Chat)
    message.chat.id = 12345
    message.from_user = MagicMock(spec=User)
    message.from_user.id = 67890
    message.from_user.first_name = "TestUser"
    message.text = ""
    message.reply = AsyncMock()
    message.answer = AsyncMock()
    return message

@pytest.fixture
def update(mock_message):
    """Create an Update object containing the mocked message."""
    update = MagicMock(spec=Update)
    update.message = mock_message
    update.effective_message = mock_message
    update.effective_chat = mock_message.chat
    update.effective_user = mock_message.from_user
    return update

@pytest.fixture
def dispatcher(mock_bot):
    """Return a Dispatcher with the mocked bot."""
    dp = Dispatcher()
    dp.bot = mock_bot
    return dp
