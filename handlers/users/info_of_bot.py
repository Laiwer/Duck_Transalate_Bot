from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import text



@dp.message_handler(Text(equals=["Инструкция"]))
async def print_language(message: Message):
    if not(existe_user_in_data_base(message.from_user.id)):
        await message.answer(text="Отправьте мне команду /start")
    else:
        await message.answer_sticker("CAACAgIAAxkBAAEDselh46rQ-UvPOgZV9vfTLn64ZQLHyAAC9wADVp29CgtyJB1I9A0wIwQ")
        instruction=text(f"Привет, {message.from_user.full_name}!\n\n",
                        "Это краткая инструкция по использованию меня.\n",
                        "Если ты нажмёшь на кнопку <u><b>\"Какой сейчас язык\"</b></u>, то я скажу тебе какой сейчас выбран язык для перевода.\n\n",
                        "Нажав на кнопку <u><b>\"Выбор языка\"</b></u>, ты с помощью клавитуры выберешь язык.",
                        "Нажимая на \"&gt&gt&gt\" и \"&lt&lt&lt\" ты можешь перемещаться по страницам, а на какой странице ты сейчас ты сможешь увидеть в сообщении.\n\n",
                        "Если ты нажмёшь на кнопку <u><b>\"Определить язык\"</b></u>, то написав мне текст я определю язык данного текста.\n\n",
                        "Меня также можно использовать в инлайн-режиме. ",
                        "<u><b>Инлайн-режим</b></u> - это когда ты можешь в другом чате, не добавля бота в этот чат, пишешь в строке сообщения адрес бота",
                        "(@duck_translate_bot) и через пробел пишешь текст, который тебе надо перевести.",
                        "Также ты можешь заметить во время набора текста в инлайн-режиме в вверху(над переведённым текстом) есть строка",
                        "\"Поменять язык\" и ты сразу можешь перейти к боту и выбрать язык.\n\n",
                        "Посмотреть эту инструкцию снова ты можешь нажать на кнопку \"Инструкция\".")
        await message.answer(text=instruction, parse_mode="html")