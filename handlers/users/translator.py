from typing import Text
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from loader import dp, tsl
from aiogram.types import Message
from states.translateState import TranslateStates
from aiogram.utils.markdown import hbold, text
from dataBase.base import get_lang_from_data_base
from data.dict_lang import Lang


@dp.message_handler(Text(equals=["📖Перевести📖"]))
async def translatorState1(message: Message):
    await message.answer(text=text(
        "Напишите текст",
        "\nНачальный язык: ", hbold(get_lang_from_data_base(message.from_user.id, "from_lang")),
        "\nПереводимый язык: ", hbold(get_lang_from_data_base(message.from_user.id, "to_lang"))))
    await TranslateStates.Q1.set()


@dp.message_handler(state=TranslateStates.Q1)
async def translatorState2(message: Message, state: FSMContext):
    itog = tsl.translate(message.text,
    src=Lang[get_lang_from_data_base(message.from_user.id, "from_lang")],
    dest=Lang[get_lang_from_data_base(message.from_user.id, "to_lang")])

    await message.answer(
        text=f"{hbold(message.text)}\nв переводе будет\n{hbold(itog.text)}"
    )
    await state.finish()