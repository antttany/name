import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS button_state (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            button TEXT NOT NULL,
            state TEXT
        );
    ''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
