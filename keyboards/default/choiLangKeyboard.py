from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.dictLang import listLangKeys


choiLang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✔Начальный язык👅"),
            KeyboardButton(text="🔄Переводимый язык👅"),
        ],
        [
            KeyboardButton(text="❌Отмена❌"),
        ]
    ],
    resize_keyboard=True
)


choiceLanguage = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=listLangKeys[0]),
            KeyboardButton(text=listLangKeys[1]),
            KeyboardButton(text=listLangKeys[2]),
        ],
        [
            KeyboardButton(text=listLangKeys[3]),
        ]
    ],
    resize_keyboard=True
)