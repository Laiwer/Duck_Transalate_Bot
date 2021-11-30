import logging

from aiogram import Dispatcher

from data.dataConfig import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)

async def on_shutdown_notify(dp:Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Выключился")

        except Exception as err:
            logging.exception(err)