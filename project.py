import os
import telebot
API_KEY=os.getenv('API_KEY')
bot=telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,'hiii! this is Quirkyy')

@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id,'Hello! Quirkyy this side')
bot.polling()