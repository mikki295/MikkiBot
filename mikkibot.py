import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from bot import tempparit


def main():

    load_dotenv()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO
    )

    updater = Updater(token = os.getenv('TOKEN'))

    command_handlers = [
        CommandHandler('tempparit',tempparit, pass_args=True)
    ]


main()