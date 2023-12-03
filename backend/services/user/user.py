import re

from backend.services.db.conn import get_cursor_conn

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
GUEST_ID = 'guest'

def register_user(name, email, password):
    if len(name) == 0 or len(email) == 0 or len(password) == 0:
        raise Exception('Invalid registration data.')

    if not re.fullmatch(EMAIL_REGEX, email):
        raise Exception('Invalid email.')

    cursor, conn = get_cursor_conn()

    data = (name, email, password)
    cursor.execute("""
        INSERT INTO users(name, email, password) VALUES(?, ?, ?)
    """, data)
    conn.commit()

    return cursor.lastrowid


def login(is_guest, email, password):
    if is_guest:
        return {'id': GUEST_ID, 'name': GUEST_ID, 'email': 'N/A'}
    else:
        cursor, _ = get_cursor_conn()
        result = cursor.execute(f"SELECT id, name, email from users where email='{email}' and password='{password}'")
        result = result.fetchone()

        if not result:
            raise Exception("Invalid login details.")

        id, name, _ = result
        return {'id': id, 'name': name, 'email': email}
