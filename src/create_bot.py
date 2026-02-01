import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import Config, RepositoryEnv


class BotHandler:
    def __init__(self):
        self.setup_logging()
        self.config = self.load_config()
        self.admins = self.load_admins()
        self.bot = self.create_bot()
        self.dp = self.create_dispatcher()

    def setup_logging(self) -> None:
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)

    def load_config(self):
        """Load configuration from ../.env file."""
        # Get the parent directory (one level up from src)
        current_dir = Path(__file__).parent
        parent_dir = current_dir.parent
        env_file = parent_dir / ".env"

        if not env_file.exists():
            raise FileNotFoundError(f".env file not found at: {env_file}")

        # Use decouple's Config with explicit path
        config = Config(RepositoryEnv(str(env_file)))
        return config

    def load_admins(self) -> list:
        """Load admin IDs from configuration."""
        try:
            admins_str = self.config("ADMINS", default="")
            return [
                int(admin_id.strip())
                for admin_id in admins_str.split(",")
                if admin_id.strip()
            ]
        except Exception as e:
            self.logger.error(f"Error loading admins: {e}")
            return []

    def create_bot(self) -> Bot:
        """Create bot instance."""
        token = self.config("TOKEN")
        if not token:
            raise ValueError("Bot token not found in environment variables")

        return Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    def create_dispatcher(self) -> Dispatcher:
        """Create dispatcher instance."""
        return Dispatcher(storage=MemoryStorage())
