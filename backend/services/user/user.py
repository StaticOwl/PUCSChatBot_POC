from backend.services.db.conn import get_cursor_conn


def register_user(name, email, password):
    cursor, conn = get_cursor_conn()

    data = (name, email, password)
    cursor.execute("""
        INSERT INTO users(name, email, password) VALUES(?, ?, ?)
    """, data)
    conn.commit()

    return cursor.lastrowid


def login(is_guest, email, password):
    if is_guest:
        return {'id': 'guest', 'name': 'guest', 'email': 'N/A'}
    else:
        cursor, _ = get_cursor_conn()
        result = cursor.execute(f"SELECT id, name, email from users where email='{email}' and password='{password}'")
        result = result.fetchone()

        if not result:
            raise Exception("Invalid login details.")

        id, name, _ = result
        return {'id': id, 'name': name, 'email': email}
