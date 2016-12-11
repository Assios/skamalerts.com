import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE emails (email TEXT, token TEXT)')

conn.close()
