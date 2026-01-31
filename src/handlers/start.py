from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.keyboard import days_kb, main_kb

classlist = [
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
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

start_router = Router()


def class_keyboard(number):
    @start_router.message(F.text == number)
    async def cmd_10b(message: Message):
        await message.answer("Выбери день", reply_markup=days_kb(number))


def choose_class():
    for i in classlist:
        class_keyboard(i)


def send_schedule(days, number):
    @start_router.message(F.text == f"{days} {number}")
    async def send_schedule(message: Message):
        await message.answer(f"Расписание на {days} {number}")
        # await message.answer()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Запуск бота с расписанием, Выберите класс",
        reply_markup=main_kb(message.from_user.id),
    )


choose_class()


@start_router.message(F.text == "Поменять класс")
async def change_class(message: Message):
    await message.answer("Выбери класс", reply_markup=main_kb(message.from_user.id))


for i in classlist:
    for j in days:
        send_schedule(j, i)
