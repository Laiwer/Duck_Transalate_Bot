from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.markdown import hbold, text
from loader import dp, tsl
from states.detecLangState import langDetect
from data.dict_lang import Lang, get_key


@dp.message_handler(Text(equals=["🤖Определить язык👅"]))
async def language_find1(message: Message):
    await message.answer(text=hbold("Введите текст"))

    await langDetect.Q1.set()


@dp.message_handler(state=langDetect.Q1)
async def language_find2(message: Message, state: FSMContext):
    itog = tsl.detect(message.text).lang
    try:
        await message.answer(text=get_key(Lang, itog))
    except:
        await message.answer(text=text(f"{itog}", "\nТакого языка нету в моей базе данных!"))

    await state.finish()