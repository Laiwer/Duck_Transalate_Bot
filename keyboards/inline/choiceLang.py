from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import dict_lang as dt


choicePage1 = InlineKeyboardMarkup(row_width=2)
choicePage2 = InlineKeyboardMarkup(row_width=2)
choicePage3 = InlineKeyboardMarkup(row_width=2)
choicePage4 = InlineKeyboardMarkup(row_width=2)
choicePage5 = InlineKeyboardMarkup(row_width=2)
choicePage6 = InlineKeyboardMarkup(row_width=2)
choicePage7 = InlineKeyboardMarkup(row_width=2)
k = 1
for i in dt.Lang:
    if k < 17 and k > 0:
        if k % 2 != 0:
            tmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
        else:
            nowTmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
            choicePage1.add(tmp, nowTmp)
        # print(1, k, i)
        k+=1
        if k == 16:
            choicePage1.add(InlineKeyboardButton(text=">>>", callback_data="pos:up:2"))
            k+=1
    if k > 16 and k < 37:
        if k % 2 != 0:
            tmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
        else:
            nowTmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
            choicePage2.add(tmp, nowTmp)
        # print(2, k, i)
        k+=1
        if k == 36:
            choicePage2.add(InlineKeyboardButton(text="<<<", callback_data="pos:down:1"),
            InlineKeyboardButton(text=">>>", callback_data="pos:up:3"))
            k+=1
    if k > 36 and k < 57:
        if k % 2 != 0:
            tmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
        else:
            nowTmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
            choicePage3.add(tmp, nowTmp)
        # print(3, k, i)
        k+=1
        if k == 56:
            choicePage3.add(InlineKeyboardButton(text="<<<", callback_data="pos:down:2"),
            InlineKeyboardButton(text=">>>", callback_data="pos:up:4"))
            k+=1
    if k > 56 and k < 77:
        if k % 2 != 0:
            tmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
        else:
            nowTmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
            choicePage4.add(tmp, nowTmp)
        # print(4, k, i)
        k+=1
        if k == 76:
            choicePage4.add(InlineKeyboardButton(text="<<<", callback_data="pos:down:3"),
            InlineKeyboardButton(text=">>>", callback_data="pos:up:5"))
            k+=1
    if k > 76 and k < 97:
        if k % 2 != 0:
            tmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
        else:
            nowTmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
            choicePage5.add(tmp, nowTmp)
        # print(5, k, i)
        k+=1
        if k == 96:
            choicePage5.add(InlineKeyboardButton(text="<<<", callback_data="pos:down:4"),
            InlineKeyboardButton(text=">>>", callback_data="pos:up:6"))
            k+=1
    if k > 96 and k < 114:
        if k % 2 != 0:
            tmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
        else:
            nowTmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
            choicePage6.add(tmp, nowTmp)
        # print(6, k, i)
        k+=1
        if k == 113:
            choicePage6.add(InlineKeyboardButton(text="<<<", callback_data="pos:down:5"),
            InlineKeyboardButton(text=">>>", callback_data="pos:up:7"))
            k+=1
    if k > 113 and k < 120:
        if k % 2 != 0:
            tmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
        else:
            nowTmp = InlineKeyboardButton(text=i.capitalize(), callback_data="lc:"+dt.Lang[i]+":+")
            choicePage7.add(tmp, nowTmp)
        # print(7, k, i)
        k+=1
        if k == 119:
            choicePage7.add(InlineKeyboardButton(text="<<<", callback_data="pos:down:6"))
            k+=1