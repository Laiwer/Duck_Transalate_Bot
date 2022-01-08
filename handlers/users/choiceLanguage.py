from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import Message
from loader import dp
from aiogram.utils.markdown import text, hbold
from states.choiLangFrom import langFrom
from states.choiLangTo import langTo
from keyboards.inline.choiceLang import choice
from data.dict_lang import Lang
from dataBase.base import get_lang_from_data_base, update_lang_in_data_base


@dp.message_handler(Text(equals=["Выбор языка"]))
async def choiceLang(message: Message):
    await message.answer(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(message.from_user.id))), reply_markup=choice)


@dp.message_handler()
