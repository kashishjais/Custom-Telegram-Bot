import os
import string
import telebot
import constants as keys
import telegram.ext
from telebot import types, TeleBot
from telebot.types import Update
from newsapi.newsapi_client import NewsApiClient
from telegram.ext import *
import requests
from news import business_news, entertainment_news, news, science_news, sports_news, technology_news

def main():
	updater=Update(keys.API_KEY)
	

bot=telebot.TeleBot(keys.API_KEY,threaded=False)
@bot.message_handler(commands=['Greet','greet'])
def greet(message):
    bot.reply_to(message,'hiii! this is Quirkyy')
@bot.message_handler(commands=['intro','who are you?'])
def greet(message):
    bot.reply_to(message,'I am  Quirkyy,your Bot assisstent🐱‍💻')    

@bot.message_handler(commands=['Hello','hello','hii','Hii'])
def hello(message):
    bot.send_message(message.chat.id,'Hello! Quirkyy this side')

@bot.message_handler(commands=['?'])
def intro(message):
    bot.send_message(message.chat.id,'I am Volter Bot')

@bot.message_handler(commands=['who created you?','creator'])
def greet(message):
    bot.reply_to(message,'Kashish Jaiswal👩🏻\n\nBtech CSE💻(2019-23)\n\nPython Data Science project🐍')


@bot.message_handler(commands=['choose'])
def intro(message):
    bot.send_message(message.chat.id,'enter news category')

@bot.message_handler(commands=['instaid'])
def instaid(message):
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


@bot.message_handler(commands=['news'])
def command_news(message):
    data = news()
    if isinstance(data,list):
        bot.reply_to(message,"\n".join(data))
    else:
        bot.reply_to(message,"No news available")

@bot.message_handler(commands=['business','Business'])
def command_news(message):
    data = business_news()
    if isinstance(data,list):
        bot.reply_to(message,"\n".join(data))
    else:
        bot.reply_to(message,"No news available")


@bot.message_handler(commands=['entertainment'])
def command_news(message):
    data = entertainment_news()
    if isinstance(data,list):
        bot.reply_to(message,"\n".join(data))
    else:
        bot.reply_to(message,"No news available")

@bot.message_handler(commands=['technology'])
def command_news(message):
    data = technology_news()
    if isinstance(data,list):
        bot.reply_to(message,"\n".join(data))
    else:
        bot.reply_to(message,"No news available")

@bot.message_handler(commands=['science'])
def command_news(message):
    data = science_news()
    if isinstance(data,list):
        bot.reply_to(message,"\n".join(data))
    else:
        bot.reply_to(message,"No news available")

@bot.message_handler(commands=['sports'])
def command_news(message):
    data = sports_news()
    if isinstance(data,list):
        bot.reply_to(message,"\n".join(data))
    else:
        bot.reply_to(message,"No news available")
bot.polling()    
    

	


									    

