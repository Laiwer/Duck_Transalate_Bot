from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


langKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧Английский🇬🇧", callback_data="tran:en"),
            InlineKeyboardButton(text="🇷🇺Русский🇷🇺", callback_data="tran:ru")
        ]
    ]
)