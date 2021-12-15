from loader import dp, tsl
from aiogram.types import Message
from aiogram.utils.markdown import hbold, text, hitalic
from dataBase.base import get_lang_from_data_base
from data.dict_lang import Lang


@dp.message_handler()
async def translatorState2(message: Message):
    itog = tsl.translate(message.text,
    src=Lang[get_lang_from_data_base(message.from_user.id, "from_lang")],
    dest=Lang[get_lang_from_data_base(message.from_user.id, "to_lang")])

    await message.answer(text=text(
        "\nНачальный язык: ", hbold(get_lang_from_data_base(message.from_user.id, "from_lang")),
        "\nПереводимый язык: ", hbold(get_lang_from_data_base(message.from_user.id, "to_lang"))))
    await message.answer(text=f"{hbold(message.text)}")
    await message.answer(text=hitalic("в переводе будет"))
    await message.answer(text=f"{hbold(itog.text)}")