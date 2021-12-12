import os
import telebot
import time

API_KEY='5089223454:AAH6ADkjcBQbRWkhJErpixgSkEj1weh8WI4'
bot=telebot.TeleBot(token=API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,'hiii! this is Quirkyy')

@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id,'Hello! Quirkyy this side')

@bot.message_handler(commands=['Help'])
def help(message):
    bot.reply_to(message,'to use this bot,send your username')    

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text
@bot.message_handler(func=lambda msg:msg.text is not None and '@'  in msg.text)
def at_answer(message):
    texts=message.text.split()
    at_text=find_at(texts)
    bot.reply_to(message,'https://instagram.com/{}'.format(at_text[1:]))
bot.polling()