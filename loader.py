from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googletrans import Translator
from data.config_data import BOT_TOKEN, ip
from pymongo import MongoClient


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

tsl = Translator()  # service_urls=['translate.googleapis.com']

cluster = MongoClient(ip)
db = cluster["dataBase"]
coll = db["collection1"]