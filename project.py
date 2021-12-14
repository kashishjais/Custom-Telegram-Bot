import os
import telebot
import constants as keys
import telegram.ext
from datetime import datetime
from telebot import types, TeleBot
from telebot.types import Update
from newsapi.newsapi_client import NewsApiClient

def main():
    updater=Update(keys.API_KEY)
    

bot=telebot.TeleBot(keys.API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,'hiii! this is Quirkyy')

@bot.message_handler(commands=['Hello','hello','hii','Hii'])
def hello(message):
    bot.send_message(message.chat.id,'Hello! Quirkyy this side')

@bot.message_handler(commands=['?'])
def intro(message):
    bot.send_message(message.chat.id,'I am Volter Bot')

def sample_responses(input_text):
    user_message=str(input_text).lower()
    if user_message in ("time","Time","time?"):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y,%H:%M:%S")
        return str(date_time)

def handle_message(update,context):
    text=str(update.message.text).lower()
    response=sample_responses(text)
    update.message.reply_text(response)        

@bot.message_handler(commands=['help','Help'])
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


# Init
newsapi = NewsApiClient(api_key='18b3064537594d28bccda78d7c20c1a7')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='in')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.in,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
print(top_headlines)