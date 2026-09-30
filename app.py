#practical 6: Identify the vulnerability in the code and fix it
#manual code:
import sqlite3
def get_user(name):
conn = sqlite3.connect("db.sqlite")
query = "SELECT * FROM users WHERE name = '" + name + "'"
return conn.execute(query).fetchall()
name = input("Enter username: ")
print(get_user(name))



# Github vulnerability code
import sqlite3
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
