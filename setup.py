import sqlite3 as sql

conn = sql.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS emails (email TEXT, token TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS posts (post TEXT)')
conn.close()
