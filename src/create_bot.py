import logging
from pathlib import Path
from typing import List

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import Config, RepositoryEnv

# Load config from ../.env
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
env_file = parent_dir / ".env"

if not env_file.exists():
    raise FileNotFoundError(f".env file not found at: {env_file}")

config = Config(RepositoryEnv(str(env_file)))


# Global admins list
def get_admins() -> List[int]:
    """Get admin IDs from configuration."""
    admins_str = config("ADMINS", default="")
    if not admins_str:
        return []
    return [
        int(admin_id.strip()) for admin_id in admins_str.split(",") if admin_id.strip()
    ]


admins: List[int] = get_admins()


class BotHandler:
    def __init__(self):
        self.setup_logging()
        self.bot = self.create_bot()
        self.dp = self.create_dispatcher()

    def setup_logging(self) -> None:
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)

    def create_bot(self) -> Bot:
        """Create bot instance."""
        token = config("TOKEN")
        if not token:
            raise ValueError("Bot token not found in environment variables")

        return Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    def create_dispatcher(self) -> Dispatcher:
        """Create dispatcher instance."""
        return Dispatcher(storage=MemoryStorage())


# Create global bot handler instance
bot_handler = BotHandler()
