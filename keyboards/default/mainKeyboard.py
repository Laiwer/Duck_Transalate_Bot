from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Какой язык сейчас"),
            KeyboardButton(text="Выбор языка"),
        ],
        [
            KeyboardButton(text="Определить язык")
        ]
    ],
    resize_keyboard=True
)