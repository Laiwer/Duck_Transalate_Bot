from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import text, hbold
from dataBase.base import get_lang_from_data_base


@dp.message_handler(Text(equals=["👅Язык👅"]))
async def print_language(message: Message):
    await message.answer(text=text(
        "\nНачальный язык: ", hbold(get_lang_from_data_base(message.from_user.id, "from_lang")),
        "\nПереводимый язык: ", hbold(get_lang_from_data_base(message.from_user.id, "to_lang"))))