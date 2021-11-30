from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖Перевести📖")
        ]
    ],
    resize_keyboard=True
)