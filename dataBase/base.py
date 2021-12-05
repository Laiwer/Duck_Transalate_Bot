import sqlite3


class BotDb():
    def __init__(self, dbFile):
        self.conn = sqlite3.connect(dbFile)
        self.cursor = self.conn.cursor()

    def get_is_reg_user(self, user_id):
        result = self.cursor.execute("SELECT id FROM user WHERE user_id == ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id, full_name):
        self.cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, full_name))
        self.cursor.execute("INSERT INTO records VALUES (?, ? ?)", (user_id, 'русский', 'английский'))
        return self.conn.commit()

    def set_languages(self,user_id, from_lang, to_lang):
        if from_lang is None:
            self.cursor.execute("UPDATE records SET to_lang = ? WHERE user_id = ?", (to_lang, user_id))
        elif to_lang is None:
            self.cursor.execute("UPDATE records SET from_lang = ? WHERE user_id = ?", (from_lang, user_id))
        return self.conn.commit()

    def get_languages(self, user_id, language="f"):
        from_lang = self.cursor.execute("SELECT from_lang FROM records WHERE user_id = ?", (user_id,))
        to_lang = self.cursor.execute("SELECT to_lang FROM records WHERE user_id = ?", (user_id,))
        # условие в одну строчку
        return from_lang if language == "f" else to_lang