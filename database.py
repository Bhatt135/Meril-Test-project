import sqlite3

def create_db():
    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            raw_text TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_candidate(data):
    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO candidates (name, email, phone, raw_text)
        VALUES (?, ?, ?, ?)
    ''', (data["name"], data["email"], data["phone"], data["raw_text"]))
    conn.commit()
    conn.close()
