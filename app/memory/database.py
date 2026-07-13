import sqlite3

connection = sqlite3.connect("jarvis.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT
)
""")

connection.commit()