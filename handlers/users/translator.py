from typing import Text
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from loader import dp, tsl, dbBot
from aiogram.types import Message
from states.translateState import TranslateStates
from aiogram.utils.markdown import hbold, text


@dp.message_handler(Text(equals=["📖Перевести📖"]))
async def translatorState1(message: Message):
    await message.answer(text=text(
        "Напишите текст",
        "\nНачальный язык: ", hbold(dbBot.get_languages(message.from_user.id, language="f")),
        "\nПереводимый язык: ", hbold(dbBot.get_languages(message.from_user.id, language="t"))))
    await TranslateStates.Q1.set()


@dp.message_handler(state=TranslateStates.Q1)
async def translatorState2(message: Message, state: FSMContext):

    itog = tsl.translate(message.text,
    src=dbBot.get_languages(message.from_user.id, language="f"),
    dest=dbBot.get_languages(message.from_user.id, language="t"))

    await message.answer(
        text=f"{hbold(message.text)}\nв переводе будет\n{hbold(itog.text)}"
    )
    await state.finish()