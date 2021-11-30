from typing import Text
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from loader import dp, tsl
from aiogram.types import Message
from states.translateState import TranslateStates
from aiogram.utils.markdown import hbold
import loader as l


@dp.message_handler(Text(equals=["📖Перевести📖"]))
async def translatorState1(message: Message, state: FSMContext):
    await message.answer(text="Напишите слово или придложение или текст, который хотите перевести")
    await TranslateStates.Q1.set()


@dp.callback_query_handler(state=TranslateStates.Q1)
async def translatorState3(message: Message, state: FSMContext):
    itog = tsl.translate(message.text, src=l.fromLang, dest=l.toLang)
    await message.answer(
        text=f"{hbold(message.text)}\nв переводе будет\n{hbold(itog.text)}"
    )
    await state.finish()