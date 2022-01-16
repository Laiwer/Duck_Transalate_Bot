from aiogram.dispatcher.filters import Text
from aiogram.types.message import Message
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.utils.markdown import text, hbold
from keyboards.inline.choiceLang import choicePage1, choicePage2, choicePage3, choicePage4, choicePage5, choicePage6, choicePage7
from dataBase.base import get_lang_from_data_base, update_lang_in_data_base, existe_user_in_data_base
from keyboards.inline.base_structure_callback_datas import langCodeCallback as lCC
from data.dict_lang import get_key, Lang


@dp.message_handler(Text(equals=["Выбор языка"]))
async def choiceLang(message: Message):
    if not(existe_user_in_data_base(message.from_user.id)):
        await message.answer(text="Отправьте мне команду /start")
    else:
        await message.answer_sticker("CAACAgIAAxkBAAEDqGBh3E5llL9di62YGKkJVZQ43Rvu_gACAgEAAladvQpO4myBy0Dk_yME")
        await message.answer(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(message.from_user.id).capitalize()),
        "\nСтраница", hbold("1/7")),
        reply_markup=choicePage1)

dp.register_message_handler(choiceLang, CommandStart(deep_link="choice"), state="*")


@dp.callback_query_handler(text_contains="pos:up")
async def up_to_pg_2_func(call: CallbackQuery):
    await call.answer(cache_time=1)
    if call.data[-1] == "2":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("2/7")),
        reply_markup=choicePage2)
    if call.data[-1] == "3":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("3/7")),
        reply_markup=choicePage3)
    if call.data[-1] == "4":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("4/7")),
        reply_markup=choicePage4)
    if call.data[-1] == "5":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("5/7")),
        reply_markup=choicePage5)
    if call.data[-1] == "6":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("6/7")),
        reply_markup=choicePage6)
    if call.data[-1] == "7":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("7/7")),
        reply_markup=choicePage7)


@dp.callback_query_handler(text_contains="pos:down")
async def down_to_pg_1_func(call: CallbackQuery):
    await call.answer(cache_time=1)
    if call.data[-1] == "1":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("1/7")),
        reply_markup=choicePage1)
    if call.data[-1] == "2":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("2/7")),
        reply_markup=choicePage2)
    if call.data[-1] == "3":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("3/7")),
        reply_markup=choicePage3)
    if call.data[-1] == "4":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("4/7")),
        reply_markup=choicePage4)
    if call.data[-1] == "5":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("5/7")),
        reply_markup=choicePage5)
    if call.data[-1] == "6":
        await call.message.edit_text(text=text(
        "Сейчас язык: ", hbold(get_lang_from_data_base(call.from_user.id).capitalize()),
        "\nСтраница", hbold("6/7")),
        reply_markup=choicePage6)


@dp.callback_query_handler(lCC.filter(in_func="+"))
async def choice_language_for_user(call: CallbackQuery):
    await call.answer(cache_time=1)
    update_lang_in_data_base(call.from_user.id, get_key(Lang, call.data[3:-2]))
    await call.message.edit_text(text=text("Установлен новый язык: ",
    hbold(get_lang_from_data_base(call.from_user.id).capitalize())))