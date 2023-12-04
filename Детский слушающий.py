import telebot as t
import datetime as dt
import time

registr = {}
adress = -1001593018324
bot = t.TeleBot('')

@bot.message_handler(commands=['PROVERKA'])
def start(message):
    x = message.id
    y = message.chat.id
    print(message.chat.id)
    bot.delete_message(y, x)



bot.polling()