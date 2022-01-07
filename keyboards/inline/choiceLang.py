from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import dict_lang as dt


choice = InlineKeyboardMarkup(row_width=2)
k = 0
for i in dt.Lang:
    choice.add(InlineKeyboardButton(text=i, callback_data=dt.Lang[i]))
    k+=1
    if k == 10:
        break