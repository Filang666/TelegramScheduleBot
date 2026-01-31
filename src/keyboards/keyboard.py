from aiogram.fsm.storage.base import KeyBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from typing_extensions import Text

from create_bot import admins


def main_kb(user_telegram_id: int):
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
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="Админ панель")])
    return ReplyKeyboardMarkup(
        keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True
    )


def days_kb(number):
    days_kb_list = [
        [KeyboardButton(text="Понедельник " + number)],
        [KeyboardButton(text="Вторник " + number)],
        [KeyboardButton(text="Среда " + number)],
        [KeyboardButton(text="Четверг " + number)],
        [KeyboardButton(text="Пятница " + number)],
        [KeyboardButton(text="Суббота " + number)],
        [KeyboardButton(text="Поменять класс")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=days_kb_list, resize_keyboard=True, one_time_keyboard=True
    )
