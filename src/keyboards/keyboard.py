import os
import sys
from typing import List, Optional

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from create_bot import admins


class KeyboardManager:
    def __init__(self):
        self.class_list: List[str] = [
            "11А",
            "11Б",
            "10А",
            "10Б",
            "9Б",
            "9А",
            "8Б",
            "8А",
            "7Б",
            "7А",
            "6Б",
            "6А",
            "5Б",
            "5А",
        ]

    def main_keyboard(self, user_telegram_id: int) -> ReplyKeyboardMarkup:
        """Create main keyboard with class selection."""
        kb_list = []

        # Add class buttons in pairs (for better layout)
        for i in range(0, len(self.class_list), 2):
            row = []
            if i < len(self.class_list):
                row.append(KeyboardButton(text=self.class_list[i]))
            if i + 1 < len(self.class_list):
                row.append(KeyboardButton(text=self.class_list[i + 1]))
            if row:
                kb_list.append(row)

        # Add admin panel button for admins
        if user_telegram_id in admins:
            kb_list.append([KeyboardButton(text="Админ панель")])

        return ReplyKeyboardMarkup(
            keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True
        )

    def days_keyboard(self, class_number: str) -> ReplyKeyboardMarkup:
        """Create days selection keyboard for a specific class."""
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
        days_kb_list = []

        # Add day buttons in pairs
        for i in range(0, len(days), 2):
            row = []
            if i < len(days):
                row.append(KeyboardButton(text=f"{days[i]} {class_number}"))
            if i + 1 < len(days):
                row.append(KeyboardButton(text=f"{days[i + 1]} {class_number}"))
            if row:
                days_kb_list.append(row)

        # Add "Change class" button
        days_kb_list.append([KeyboardButton(text="Поменять класс")])

        return ReplyKeyboardMarkup(
            keyboard=days_kb_list, resize_keyboard=True, one_time_keyboard=True
        )
