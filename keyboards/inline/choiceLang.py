from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import dict_lang as dt


choicePage1 = InlineKeyboardMarkup(row_width=1)
choicePage2 = InlineKeyboardMarkup(row_width=1)
choicePage3 = InlineKeyboardMarkup(row_width=1)
choicePage4 = InlineKeyboardMarkup(row_width=1)
choicePage5 = InlineKeyboardMarkup(row_width=1)
choicePage6 = InlineKeyboardMarkup(row_width=1)
k = 0
for i in dt.Lang:
    while k < 21:
        choicePage1.add(InlineKeyboardButton(text=i, callback_data=dt.Lang[i]))
        k+=1
        if k == 20:
            choicePage1.add(InlineKeyboardButton(text=">>>", callback_data="up_pt2"))
    while k > 20 and k < 41:
        choicePage2.add(InlineKeyboardButton(text=i, callback_data=dt.Lang[i]))
        k+=1
        if k == 40:
            choicePage2.add(InlineKeyboardButton(text="<<<", callback_data="down_pt1"),
            InlineKeyboardButton(text=">>>", callback_data="up_pt3"))