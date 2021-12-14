from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googletrans import Translator
from data import no_see_this_file_12345_data_config as nstf1dc
from pymongo import MongoClient
import dns


bot = Bot(token=nstf1dc.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

tsl = Translator()  # service_urls=['translate.googleapis.com']

cluster = MongoClient(nstf1dc.ip)
db = cluster["dataBase"]
coll = db["collection1"]