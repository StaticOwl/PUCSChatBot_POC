import os
import sqlite3

from dotenv import load_dotenv
load_dotenv()
DB_FILE = os.getenv('SQL_DB_FILE')


def get_conn():
    conn = sqlite3.connect(DB_FILE)
    return conn


def get_cursor():
    return get_conn().cursor()


def get_cursor_conn():
    conn = get_conn()
    return conn.cursor(), conn
