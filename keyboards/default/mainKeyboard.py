from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Язык"),
            KeyboardButton(text="Выбор языка"),
        ],
        [
            KeyboardButton(text="Определить язык")
        ]
    ],
    resize_keyboard=True
)