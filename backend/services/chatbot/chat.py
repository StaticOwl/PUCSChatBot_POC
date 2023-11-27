from backend.services.db.conn import get_cursor_conn
from .palm_model import test


def chat(msg, *args, **kwargs):
    user_id = kwargs.get('user_id', 'N/A')
    response, accuracy = test(msg)

    cursor, conn = get_cursor_conn()

    data = (user_id, msg, response, accuracy)
    cursor.execute("""
            INSERT INTO chats(user_id, query, response, accuracy) VALUES(?, ?, ?, ?)
        """, data)
    conn.commit()

    return response
