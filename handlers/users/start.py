from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import mainKeyboard

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    
    news = """Бот получил не сильно много изменений.
    Мы убрали команду /translator и добавили более понятную кнопку.
    Но он ещё в бета-тестировании."""
    await message.answer(text=news, reply_markup=mainKeyboard)
