from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.markdown import hbold, text
from loader import dp, tsl
from states.detecLangState import langDetect
from data.dict_lang import Lang, get_key


@dp.message_handler(Text(equals=["Определить язык"]))
async def language_find1(message: Message):
    await message.answer_sticker("CAACAgIAAxkBAAEDqGJh3E668vnJSjLC81kZRP62cAb2dgAC-QADVp29CpVlbqsqKxs2IwQ")
    await message.answer(text=hbold("Введите текст, у которого надо определить язык"))

    await langDetect.Q1.set()


@dp.message_handler(state=langDetect.Q1)
async def language_find2(message: Message, state: FSMContext):
    itog = tsl.detect(message.text).lang
    try:
        await message.answer(text=hbold(get_key(Lang, itog).capitalize()))
    except:
        await message.answer(text=text(f"{itog}", "\nЧто-то не так!"))
    
    await state.finish()