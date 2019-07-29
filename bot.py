from ohjelma import get_info, get_week_schedule

def __send_message(bot, update, message):
    bot.send_message(chat_id=update.message.chat_id, text='Hetki pieni', parse_mode='markdown')
    bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode='markdown')


def tempparitToday(bot, update, args):
    __send_message(bot, update, get_info())

def tempparitSchedule(bot, update, args):
    __send_message(bot,update, get_week_schedule())
