from loader import coll
from data.dict_lang import listLangKeys
from datetime import datetime


def existe_user_in_data_base(user_id):
    return bool(coll.count_documents({"user__id": user_id}))


def add_user_in_data_base(user_id, user_name, full_name):
    dt = datetime.now()
    time = f"{dt.hour}:{dt.minute}:{dt.second} | {dt.day}.{dt.month}.{dt.year}"
    user_info = {
        "user__id": user_id,
        "user_name": user_name,
        "full_name": full_name,
        "date_reg": time,
        "from_lang": listLangKeys[0],
        "to_lang": listLangKeys[1]
    }
    coll.insert_one(user_info)


def get_lang_from_data_base(user_id, lang):
    return coll.find_one({"user__id": user_id})[lang]


def update_lang_in_data_base(user_id, why_lang, lang):
    coll.update_one({"user__id": user_id}, {"$set": {why_lang: lang}})
