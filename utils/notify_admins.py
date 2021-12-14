import logging

from aiogram import Dispatcher

from data import no_see_this_file_12345_data_config as nstf1dc


async def on_startup_notify(dp: Dispatcher):

    for admin in nstf1dc.ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)

async def on_shutdown_notify(dp:Dispatcher):
    for admin in nstf1dc.ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Выключился")

        except Exception as err:
            logging.exception(err)

# 