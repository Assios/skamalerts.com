from flask import Flask, render_template, request
from validate_email import validate_email
import sqlite3 as sql
import uuid
import sys
from mail import send_welcome_mail

app = Flask(__name__)


def token():
    return uuid.uuid4().hex


def verify_email_token_exists(email, token):
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM emails')
    rows = c.fetchall()
    c.close()

    return (email, token) in rows


def fetch_emails():
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute('SELECT email FROM emails')
    rows = c.fetchall()
    c.close()
    return [row[0] for row in rows]


@app.route('/')
def home():
    return render_template('index.html', share_button=True)


@app.route('/unsubscribe')
def unsubscribe():
    email = request.args.get('email')
    token = request.args.get('token')

    if email and token and verify_email_token_exists(email, token):
        return render_template('unsubscribe.html', email=email, token=token)
    else:
        return render_template('unsubscribe_fail.html')


@app.route('/unsub', methods=['POST'])
def unsub():
    ugyldig = False
    duplicate = False
    success = False

    try:
        email = request.form['email']
        token = request.form['token']

        if email and token and verify_email_token_exists(email, token):
            c = sql.connect("database.db")
            c.execute("DELETE FROM emails WHERE email=? AND token=?", (email, token))
            c.commit()
            print "DELETED %s" % email
            msg = "%s vil ikke lenger motta Skam-oppdateringer. Du kan sende inn eposten din igjen hvis du ombestemmer deg!" % email
            color = "#4F8A10"
            unsubbed = True
            return render_template("index.html", msg=msg, color=color, ugyldig=ugyldig, duplicate=duplicate,
                                   success=success, unsubbed=unsubbed)
        else:
            msg = "Noe gikk galt"
            color = "#D8000C"
            ugyldig = True
            return render_template("index.html", msg=msg, color=color, ugyldig=ugyldig, duplicate=duplicate,
                                   success=success)
    except:
        msg = "Noe gikk gaaaalt"
        color = "#D8000C"
        ugyldig = True
        return render_template("index.html", msg=msg, color=color, ugyldig=ugyldig, duplicate=duplicate,
                               success=success)


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        msg = ""
        color = ""
        ugyldig = False
        duplicate = False
        success = False

        try:
            email = request.form['email'].lower()

            if validate_email(email):
                con = sql.connect("database.db")
                cur = con.cursor()

                cur.execute('SELECT * FROM emails')
                rows = cur.fetchall()
                emails = [row[0].lower() for row in rows]

                if email in emails:
                    duplicate = True
                    msg = "Den eposten er allerede lagt til, din tulling."
                    color = "#F2A7AD"
                else:
                    tok = token()
                    cur.execute("INSERT INTO emails (email, token) VALUES (?,?)", (email, tok))
                    con.commit()
                    msg = "Eposten %s er lagt til!" % email
                    send_welcome_mail(email, tok)
                    color = "#3B732C"
                    success = True
            else:
                msg = "Ugyldig epost!"
                color = "#D8000C"
                ugyldig = True
        except:
            con.rollback()
            msg = "Kunne ikke legge til epost."

        finally:
            return render_template("index.html", msg=msg, color=color, ugyldig=ugyldig, duplicate=duplicate,
                                   success=success)
            con.close()


if __name__ == '__main__':
    app.run(debug=True)
