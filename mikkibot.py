import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from bot import tempparitToday, tempparitSchedule
from ohjelma import get_info, get_week_schedule


def main():

    load_dotenv()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO
    )

    updater = Updater(token = '962049728:AAF0f94vBresgG971TYhKdbg_qSHsRQVhIk')
    #updater = Updater(token = os.getenv('TOKEN'))
    print(get_info())

#This section is for handling telegram commands

#    command_handlers = [
#        CommandHandler('tempparit_tanaan',tempparitToday, pass_args=True),
#        CommandHandler('tempparit_viikolla',tempparitSchedule, pass_args=True)
#    ]
#
#    for handler in command_handlers:
#        updater.dispatcher.add_handler(handler)
#
#    updater.start_polling()

main()