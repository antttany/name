import sqlite3
from sqlite3 import Error

# Функция для подключения к базе данных SQLite
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

# Функция для проверки наличия айдишника в базе и возврата кнопки
def get_button_by_id(user_id, db_file):
    conn = create_connection(db_file)
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT button FROM button_state WHERE user_id = ? AND (state IS NULL OR state = '')", (user_id,))
            row = cursor.fetchone()
            if row:
                button = row[0]
                # Обновляем состояние state на True
                update_button_state(conn, user_id, "True")
                print(11111)
                return f"{button}"
            else:
                return False
        except Error as e:
            print(e)
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

# Функция для обновления состояния кнопки в базе данных
def update_button_state(conn, user_id, new_state):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE button_state SET state = ? WHERE user_id = ?", (new_state, user_id))
        conn.commit()
        print(f"State updated to {new_state} for user {user_id}")
    except Error as e:
        print(e)
