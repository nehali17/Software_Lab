#practical 6: Identify the vulnerability in the code and fix it
import sqlite3

# Github vulnerability code
def get_username(name):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result

# Windsurf vulnerability code
import sqlite3

def get_username(name):
    conn = sqlite3.connect("db.sqlite")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE name = ?", (name,))
        return cursor.fetchall()
    finally:
        conn.close()
