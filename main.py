import telebot
import asyncio
from shazamio import Shazam

TOKEN = None

with open("TOKEN") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Hello")

bot.polling()