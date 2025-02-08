import sqlite3
def getcur():
    conn = sqlite3.connect('password.db')
    cur = conn.cursor()
    return cur
def Create():
    
    cur=getcur()
    # Create users table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        email TEXT UNIQUE
    );
    ''')

    # Create password table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS password (
        password_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        website TEXT NOT NULL,
        password_text TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    ''')

   


