import sqlite3

DB_FILE = './resources/sql.db'


def get_conn():
    conn = sqlite3.connect(DB_FILE)
    return conn


def get_cursor():
    return get_conn().cursor()


def get_cursor_conn():
    conn = get_conn()
    return conn.cursor(), conn
