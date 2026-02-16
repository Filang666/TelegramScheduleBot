import pytest
from unittest.mock import AsyncMock, MagicMock
from aiogram.types import Message

# Import your handlers (adjust paths to your actual module)
from bot.handlers import start_command, help_command

@pytest.mark.asyncio
async def test_start_command(update, mock_message):
    """Test the /start command replies with a welcome message."""
    # Import the handler inside the test to avoid circular imports
    from bot.handlers import start_command

    # Set the message text to "/start" (if your handler uses it)
    mock_message.text = "/start"

    # Call the handler
    await start_command(message=mock_message, **{"some_arg_if_needed": None})

    # Assert that reply or answer was called
    mock_message.answer.assert_called_once()
    # Or if you use reply:
    # mock_message.reply.assert_called_once()

    # Check the content of the reply
    args, kwargs = mock_message.answer.call_args
    assert "Welcome" in args[0]  # adjust to your actual message
