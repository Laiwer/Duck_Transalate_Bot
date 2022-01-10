from loader import coll
from data.dict_lang import get_key
from datetime import datetime
import pytz


def existe_user_in_data_base(user_id):
    return bool(coll.count_documents({"user__id": user_id}))


def add_user_in_data_base(user_id, user_name, full_name):
    dt = datetime.now(pytz.timezone('Europe/Moscow'))
    time = f"{dt.hour}:{dt.minute}:{dt.second} | {dt.day}.{dt.month}.{dt.year}"
    user_info = {
        "user__id": user_id,
        "user_name": user_name,
        "full_name": full_name,
        "date_reg": time,
        "lang": "английский"
    }
    coll.insert_one(user_info)


def get_lang_from_data_base(user_id):
    return coll.find_one({"user__id": user_id})["lang"]


def update_lang_in_data_base(user_id, lang):
    coll.update_one({"user__id": user_id}, {"$set": {"lang": lang}})
