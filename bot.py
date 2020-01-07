import telebot
import config
import pb
import datetime
import pytz
import json
import traceback
from telebot import apihelper


P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])  
def start_command(message):  
    bot.send_message(  
        message.chat.id,  
        'Greetings! I can show you exchange rates.\n' +  
        'To get the exchange rates press /exchange.\n' +  
        'To get help press /help.'  
  )
if __name__ == '__main__':
     bot.polling(none_stop=True)

