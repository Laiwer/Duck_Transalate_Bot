from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import mainKeyboard

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message)
    if (not db.get_is_reg_user(message.from_user.id)):
        db.add_user(message.from_user.id, message.from_user.full_name)

    await message.answer(f"Привет, {message.from_user.full_name}!")
    
    news = """Из бета-теста я перешёл в стадию пре-релиза(v0.2).
Добавилось больше языков и для тебя, юзера, не заметное, но очень важное - это База Данных."""
    await message.answer(text=news, reply_markup=mainKeyboard)
