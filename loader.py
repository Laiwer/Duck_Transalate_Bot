from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googletrans import Translator
from data.config_data_top_secret import BOT_TOKEN
from dataBase.base import BotDb

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

tsl = Translator()  # service_urls=['translate.googleapis.com']

db = BotDb("dataBase/tanker.db")