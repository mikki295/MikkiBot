import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from bot import tempparit
from ohjelma import get_info, get_week_schedule


def main():

    load_dotenv()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO
    )

    updater = Updater(token = '962049728:AAF0f94vBresgG971TYhKdbg_qSHsRQVhIk')
    #updater = Updater(token = os.getenv('TOKEN'))
    #print(get_info('http://telkku.com/'))
    get_week_schedule()

#This section is for handling telegram commands

#    command_handlers = [
#        CommandHandler('tempparit',tempparit, pass_args=True)
#    ]
#
#    for handler in command_handlers:
#        updater.dispatcher.add_handler(handler)
#
#    updater.start_polling()

main()