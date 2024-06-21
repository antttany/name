from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests

# pip install python-telegram-bot==13.15
API_TOKEN = '7032123911:AAHxZ3tLrb5A4e6P3KSS36z1O4W7a3SknrQ'
clicked_button = None
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data='button1'),
            InlineKeyboardButton("Кнопка 2", callback_data='button2'),
        ],
        [
            InlineKeyboardButton("Кнопка 3", callback_data='button3'),
            InlineKeyboardButton("Кнопка 4", callback_data='button4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    original_message_text = query.message.text + '\n\nОжидайте ответа пользователя.'
    with open('button_state.txt', 'w') as f:
        f.write(query.data)
    if query.data == 'button3':
        response = requests.get('http://127.0.0.1:5000/test')
        if response.status_code == 200:
            print('ALL GOOD')
    query.edit_message_text(text=original_message_text)

def main() -> None:
    
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()