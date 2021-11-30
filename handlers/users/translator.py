from typing import Text
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from loader import dp, tsl
from aiogram.types import Message
from keyboards.inline.language import langKeyboard
from states.translateState import TranslateStates
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.markdown import hbold
import logging


@dp.message_handler(Text(equals=["📖Перевести📖"]))
async def translatorState1(message: Message, state: FSMContext):
    await message.answer(text="Напишите слово или придложение или текст, который хотите перевести")

    await TranslateStates.Q1.set()


@dp.message_handler(state=TranslateStates.Q1)
async def translatorState2(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer(text="Выбери язык, на который перевести:", reply_markup=langKeyboard)
    await TranslateStates.next()
    logging.info(f"up")


@dp.callback_query_handler(state=TranslateStates.Q2)
async def translatorState3(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    secondLang = call.data[5:]
    logging.info(f"call = {secondLang}")

    data = await state.get_data()
    logging.info(type(data))
    textTran = data["text"]

    itog = tsl.translate(textTran, dest=secondLang)

    await call.message.answer(
        text=f"{hbold(textTran)}\nв переводе будет\n{hbold(itog.text)}"
    )

    await state.finish()