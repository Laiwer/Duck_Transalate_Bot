from typing import Text
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from loader import dp, tsl, fromLang, toLang
from aiogram.types import Message
from states.translateState import TranslateStates
from aiogram.utils.markdown import hbold, text
import loader as l
from data.dictLang import Lang


@dp.message_handler(Text(equals=["📖Перевести📖"]))
async def translatorState1(message: Message):
    await message.answer(text=text("Напишите текст", "\nНачальный язык: ", hbold(fromLang), "\nПереводимый язык: ", hbold(toLang)))
    await TranslateStates.Q1.set()


@dp.message_handler(state=TranslateStates.Q1)
async def translatorState2(message: Message, state: FSMContext):
    itog = tsl.translate(message.text, src=Lang[fromLang], dest=Lang[toLang])
    await message.answer(
        text=f"{hbold(message.text)}\nв переводе будет\n{hbold(itog.text)}"
    )
    await state.finish()