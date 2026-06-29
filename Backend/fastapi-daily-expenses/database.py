import sqlite3

conn = sqlite3.connect('expenses.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    item TEXT NOT NULL,
    price INTEGER NOT NULL,
    date TEXT NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

conn.commit()