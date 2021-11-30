from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖Перевести📖"),
            KeyboardButton(text="👅Выбор языка👅"),
        ]
    ],
    resize_keyboard=True
)