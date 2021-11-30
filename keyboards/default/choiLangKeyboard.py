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
    ]
)


choiceLanguage = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="русский"),
            KeyboardButton(text="английский")
        ]
    ]
)