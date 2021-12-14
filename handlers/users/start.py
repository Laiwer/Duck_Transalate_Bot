from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import mainKeyboard
from dataBase.base import existe_user_in_data_base, add_user_in_data_base
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message)
    if not(existe_user_in_data_base(message.from_user.id)):
        add_user_in_data_base(message.from_user.id, message.from_user.username, message.from_user.full_name)

    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=mainKeyboard)
