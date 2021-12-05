from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import Message
from loader import dp, dbBot
from aiogram.utils.markdown import text, hbold
from keyboards.default.choiLangKeyboard import choiLang, choiceLanguage
from states.choiLangFrom import langFrom
from states.choiLangTo import langTo
from keyboards.default.mainKeyboard import mainKeyboard
from data.dict_lang import Lang


@dp.message_handler(Text(equals=["👅Выбор языка👅"]))
async def choiceLang(message: Message):
    await message.answer(text=text("Начальный язык: ", hbold(dbBot.get_languages(message.from_user.id, language="f")), "\nПереводимый язык: ", hbold(db.get_languages(message.from_user.id, language="t")), reply_markup=choiLang))


@dp.message_handler(Text(equals=["✔Начальный язык👅"]))
async def setFromLang1(message: Message):
    await message.answer(text="Выбери один из имеющихся языков: ", reply_markup=choiceLanguage)

    await langFrom.Q1.set()


@dp.message_handler(state=langFrom.Q1)
async def setFromLang2(message: Message, state: FSMContext):
    if message.text in list(Lang.keys()):
        db.set_languages(message.from_user.id, from_lang=message.text, to_lang=None)

        await message.answer(text="Начальный язык установлен", reply_markup=choiLang)
        await state.finish()
    else:
        await message.answer(text="Начальный язык не найден", reply_markup=choiLang)


@dp.message_handler(Text(equals=["🔄Переводимый язык👅"]))
async def setToLang1(message: Message):
    await message.answer(text="Выбери один из имеющихся языков: ", reply_markup=choiceLanguage)
    await langTo.Q1.set()


@dp.message_handler(state=langTo.Q1)
async def setToLang2(message: Message, state: FSMContext):
    if message.text in list(Lang.keys()):
        db.set_languages(message.from_user.id, from_lang=None, to_lang=message.text)

        await message.answer(text="Переводимый язык установлен", reply_markup=choiLang)
        await state.finish()
    else:
        await message.answer(text="Переводимый язык не найден", reply_markup=choiLang)


@dp.message_handler(Text(equals=["❌Отмена❌"]))
async def cancelSetLang(message: Message):
    await message.answer(text="Отмена выбора языка", reply_markup=mainKeyboard)