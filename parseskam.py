#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encoding=utf8

import sqlite3 as sql
import sys

from bs4 import BeautifulSoup
from datetime import datetime
import urllib
import threading
from mail import send_multiple_mailgun

reload(sys)
sys.setdefaultencoding('utf8')


def fetch_emails_and_tokens():
    conn = sql.connect("../database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM emails')
    all_rows = c.fetchall()
    c.close()
    return all_rows

def fetch_previous_skam_posts():
    conn = sql.connect("../database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    all_rows = c.fetchall()
    c.close()
    return [row[0] for row in all_rows]

def add_post(post):
    con = sql.connect("../database.db")
    c = con.cursor()
    c.execute("INSERT INTO posts (post) VALUES (?)", (post,))
    con.commit()
    con.close()

class Post:
    def get_type(self, article):
        link = article.find("a")
        href = link["href"]

        if article.find("div", class_="nrk-video"):
            return "video"
        if "insta" in href:
            return "instagram-post"
        else:
            return "chat"

    def convert_time(self, norwegian):
        norwegian = norwegian.split(" ", 1)[1]
        return datetime.strptime(norwegian, '%d.%m.%y kl %H.%M')

    def __init__(self, article):
        self.article = article
        self.img = article.find("img")["src"]
        self.link = article.find("a")
        self.href = self.link["href"]
        self.original_time = self.link.get_text()
        self.original_time = self.original_time.replace("ø", "o")
        self.time = self.convert_time(self.original_time)
        self.type = self.get_type(self.article)
        try:
            self.title = article.find("h2").find("a")["title"]
        except:
            self.title = ""

def skam():
    emails_and_tokens = fetch_emails_and_tokens()
    r = urllib.urlopen('http://skam.p3.no').read()
    soup = BeautifulSoup(r, "html.parser")
    articles = soup.find_all("article", class_="post")
    posts = [Post(article) for article in articles]
    print posts

    if not posts or len(posts)==0:
        print "EMPTY POSTS"
    else:
        last = posts[0]

        if not last.original_time.lower() in fetch_previous_skam_posts():
            add_post(last.original_time.lower())

            if last.type == "chat":
                img_url = "<br><img src=\"%s\"/>" % last.img
            else:
                img_url = ""

            send_multiple_mailgun(emails_and_tokens, last.title, last.href, last.original_time, last.type, img_url)
            print emails_and_tokens
            print "EMAILS SENDT!"
        else:
            print last.original_time

    threading.Timer(10.0, skam).start()

skam()
