from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import text


choiLang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Начальный язык"),
            KeyboardButton(text="Переводимый язык"),
        ],
        [
            KeyboardButton(text="Отмена"),
        ]
    ],
    resize_keyboard=True
)


choiceLanguage = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="русский"),
            KeyboardButton(text="английский")
        ]
    ],
    resize_keyboard=True
)