from loader import dp, tsl
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils.markdown import hbold
from dataBase.base import get_lang_from_data_base, existe_user_in_data_base
from . import Lang


@dp.inline_handler()
async def inline_answer(query: InlineQuery):
    try:
        if not(existe_user_in_data_base(query.from_user.id)):
            arti = [InlineQueryResultArticle(
                id=query.from_user.id,
                title="👆Перейдите к боту и начните оттуда☝",
                input_message_content=InputTextMessageContent(message_text="hello")
            )]
            await query.answer(results=arti, cache_time=1, is_personal=True,
                                switch_pm_text="Начать", switch_pm_parameter="_")
        else:
            itog = tsl.translate(query.query, dest=Lang[get_lang_from_data_base(query.from_user.id)])
            articles = [InlineQueryResultArticle(
                id=query.from_user.id,
                title=itog.text,
                description=f"Установлен язык: {get_lang_from_data_base(query.from_user.id)}\nПоменять можно нажав на кнопку выше☝",
                input_message_content=InputTextMessageContent(message_text=itog.text)
            )]
            await query.answer(results=articles, cache_time=1, is_personal=True,
                                switch_pm_text="Поменять язык", switch_pm_parameter="choice")
    except Exception as ex:
        pass