import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
import ohjelma




def main():

    load_dotenv()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO
    )


    

main()