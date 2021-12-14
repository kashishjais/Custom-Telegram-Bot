import os
import telebot
import constants as keys
import telegram.ext
from datetime import datetime
from telebot import types, TeleBot
from telebot.types import Update
from newsapi.newsapi_client import NewsApiClient

from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot.custom_filters import AdvancedCustomFilter
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import time as tm
from telebot import types

from world_time import get_time
from news import get_article


def main():
    updater=Update(keys.API_KEY)
    

bot=telebot.TeleBot(keys.API_KEY,threaded=False)

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



@bot.message_handler(commands=['start'])
def command_start(message):
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
	start_markup.row('/start', '/help', '/hide')
	start_markup.row('/world_time', '/news')
	bot.send_message(message, "🤖 The bot has started!\n⚙ Enter /help to see bot's function's")
	bot.send_message(message, "⌨️ The Keyboard is added!\n⌨️ /hide To remove kb ", reply_markup=start_markup)

@bot.message_handler(commands=['hide'])
def command_hide(message):
	hide_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message, "⌨💤...", reply_markup=hide_markup)

@bot.message_handler(commands=['help'])
def command_help(message):
	bot.send_message(message, "🤖 /start - display the keyboard\n"
									  "⌛️ /world_time - current time\n"
									  "📰 /news - latest bbc article\n")

@bot.message_handler(commands=['world_time'])
def command_world_time(message):
	sent = bot.send_message(message, "🗺 Enter the City or Country\n🔍 In such format:  Moscow  or  china")
	bot.register_next_step_handler(sent, send_time)
def send_time(message):
	try:
		get_time(message.text)
	except IndexError:
		bot.send_message(message, "❌ Wrong place, check mistakes and try again")
	time = get_time(message.text)
	bot.send_message(message, time)

@bot.message_handler(commands=['news'])
def command_news(message):
	bot.send_message(message, "🆕 Latest BBC article:\n")
	bot.send_message(message, get_article(), parse_mode='HTML')

while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		tm.sleep(10)

									    

