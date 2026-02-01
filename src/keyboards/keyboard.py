from typing import List

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class KeyboardManager:
    def __init__(self, admins: List[int]):
        self.admins = admins

    def main_keyboard(self, user_telegram_id: int) -> ReplyKeyboardMarkup:
        """Create main keyboard with class selection."""
        kb_list = [
            [KeyboardButton(text="11Б")],
            [KeyboardButton(text="11А")],
            [KeyboardButton(text="10Б")],
            [KeyboardButton(text="10А")],
            [KeyboardButton(text="9Б")],
            [KeyboardButton(text="9А")],
            [KeyboardButton(text="8Б")],
            [KeyboardButton(text="8А")],
            [KeyboardButton(text="7Б")],
            [KeyboardButton(text="7А")],
            [KeyboardButton(text="6Б")],
            [KeyboardButton(text="6А")],
            [KeyboardButton(text="5Б")],
            [KeyboardButton(text="5А")],
        ]

        if user_telegram_id in self.admins:
            kb_list.append([KeyboardButton(text="Админ панель")])

        return ReplyKeyboardMarkup(
            keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True
        )

    def days_keyboard(self, class_number: str) -> ReplyKeyboardMarkup:
        """Create days selection keyboard for a specific class."""
        days_kb_list = [
            [KeyboardButton(text=f"Понедельник {class_number}")],
            [KeyboardButton(text=f"Вторник {class_number}")],
            [KeyboardButton(text=f"Среда {class_number}")],
            [KeyboardButton(text=f"Четверг {class_number}")],
            [KeyboardButton(text=f"Пятница {class_number}")],
            [KeyboardButton(text=f"Суббота {class_number}")],
            [KeyboardButton(text="Поменять класс")],
        ]

        return ReplyKeyboardMarkup(
            keyboard=days_kb_list, resize_keyboard=True, one_time_keyboard=True
        )
