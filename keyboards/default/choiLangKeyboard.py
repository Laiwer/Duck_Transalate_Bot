from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.dict_lang import listLangKeys


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
        ],
        [
            KeyboardButton(text=listLangKeys[2]),
            KeyboardButton(text=listLangKeys[3]),
        ],
        [
            KeyboardButton(text=listLangKeys[4]),
            KeyboardButton(text=listLangKeys[5]),
        ],
        [
            KeyboardButton(text=listLangKeys[6]),
            KeyboardButton(text=listLangKeys[7]),
        ],
        [
            KeyboardButton(text=listLangKeys[8]),
            KeyboardButton(text=listLangKeys[9]),
        ],
        [
            KeyboardButton(text=listLangKeys[10]),
            KeyboardButton(text=listLangKeys[11]),
        ]
    ],
    resize_keyboard=True
)