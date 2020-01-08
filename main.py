# -*- coding: utf-8 -*-

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from bittrex import BittrexError
from bittrex import BittrexClient

from config import TG_TOKEN
from config import TG_API_URL

def do_start(bot: Bot, update: Update):
    bot.send_message(
            chat_id = update.message.chat_id,
            text = "Hi! Let's become rich!"
            )
    
def do_echo(bot: Bot, update: Update):   
    text = update.message.text
    bot.send_message(
            chat_id = update.message.chat_id,
            text = text)
           
def caps(bot: Bot, update: Update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
  
    
def unknown(bot: Bot, update: Update):
    bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def btc_usd(bot: Bot, update: Update):
    print('H')
    NOTIFY_PAIR = "USD-BTC"
    client = BittrexClient()
    try:
        current_price = client.get_last_price(NOTIFY_PAIR)
        message = "{} = {}".format(NOTIFY_PAIR, current_price)
    except BittrexError:
        message = "Error"
    print(message)
    bot.send_message(
            chat_id = update.message.chat_id,
            text = message
            )
    
    


def main():
    bot = Bot(
            token = TG_TOKEN,
            base_url = TG_API_URL,
            )
    updater = Updater(
            bot = bot,
            )

    
    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    caps_handler = CommandHandler("caps", caps, pass_args = True)
    btc_usd_hsndler = CommandHandler("btc", btc_usd)
    unknown_handler = MessageHandler(Filters.command, unknown)
    
    
    
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(caps_handler)
    updater.dispatcher.add_handler(btc_usd_hsndler)
    updater.dispatcher.add_handler(unknown_handler)
    
    
    updater.start_polling()
    #updater.idle()
    
if __name__ == '__main__':
    main()
    