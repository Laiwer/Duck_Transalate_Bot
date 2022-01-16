from loader import dp, tsl
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dataBase.base import get_lang_from_data_base, existe_user_in_data_base
from data.dict_lang import Lang


@dp.message_handler()
async def translatorState2(message: Message):
    if not(existe_user_in_data_base(message.from_user.id)):
        await message.answer(text="Отправьте мне команду /start")
    else:
        itog = tsl.translate(message.text, dest=Lang[get_lang_from_data_base(message.from_user.id)])
        await message.answer(text=f"{hbold(itog.text)}")