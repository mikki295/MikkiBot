from ohjelma import get_info

def __send_message(bot, update, message):
    bot.__send_message(chat_id=update.message.chat_id, text=message, parse_mode='markdown')


def tempparit(bot, update, args):
    __send_message(bot, update, get_info())