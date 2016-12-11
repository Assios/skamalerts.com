import sqlite3 as sql
import sys

def delete(num, db="database.db"):
    con = sql.connect(db)
    cur = con.cursor()
    cur.execute("DELETE FROM emails WHERE email=?", (email,))
    con.commit()

email = sys.argv[1]

delete(email)
