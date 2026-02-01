import os
import sys
from typing import Optional

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from create_bot import admins
from filters.filters import AdminFilter
from keyboards.keyboard import KeyboardManager
from read import PDFProcessor


class StartHandler:
    def __init__(self, router: Router):
        self.router = router
        self.keyboard_manager = KeyboardManager()
        self.pdf_processor = PDFProcessor()
        self.class_list: list[str] = self.keyboard_manager.class_list
        self.days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

        self.register_handlers()

    def register_handlers(self) -> None:
        """Register all message handlers."""

        # Start command
        @self.router.message(CommandStart())
        async def cmd_start(message: Message):
            await message.answer(
                "Запуск бота с расписанием. Выберите класс:",
                reply_markup=self.keyboard_manager.main_keyboard(message.from_user.id),
            )

        # Class selection handlers
        for class_name in self.class_list:

            @self.router.message(F.text == class_name)
            async def handle_class_selection(message: Message):
                class_num: Optional[str] = message.text
                if class_num:
                    await message.answer(
                        f"Выбран класс: {class_num}. Выберите день:",
                        reply_markup=self.keyboard_manager.days_keyboard(class_num),
                    )

        # Day selection handlers
        for day in self.days:
            for class_name in self.class_list:

                @self.router.message(F.text == f"{day} {class_name}")
                async def handle_day_selection(message: Message):
                    text: Optional[str] = message.text
                    if text:
                        parts = text.split()
                        if len(parts) >= 2:
                            day_name = parts[0]
                            class_num = parts[1]
                            schedule = self.pdf_processor.parse_schedule_text(
                                class_num, day_name
                            )
                            await message.answer(schedule)

        # Change class handler
        @self.router.message(F.text == "Поменять класс")
        async def change_class(message: Message):
            await message.answer(
                "Выберите класс:",
                reply_markup=self.keyboard_manager.main_keyboard(message.from_user.id),
            )

        # Admin panel handler (only for admins)
        @self.router.message(F.text == "Админ панель", AdminFilter())
        async def admin_panel(message: Message):
            await message.answer(
                "👨‍💼 Админ панель:\n"
                "/update_schedule - Обновить расписание\n"
                "/stats - Показать статистику\n"
                "/broadcast - Отправить сообщение всем пользователям"
            )


# Create router and handler
start_router = Router()
