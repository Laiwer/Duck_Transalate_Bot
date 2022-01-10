from aiogram.utils.callback_data import CallbackData


langPosCallback = CallbackData("pos", "ud", "pgnum")  # pos - position | ud - up or down | pgnum - page number
langCodeCallback = CallbackData("lc", "lang_code", "in_func") # lc - language code