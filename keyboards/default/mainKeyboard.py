from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Какой язык сейчас"),
            KeyboardButton(text="Выбор языка"),
        ],
        [
            KeyboardButton(text="Определить язык"),
            KeyboardButton(text="Инструкция")
        ]
    ],
    resize_keyboard=True
)