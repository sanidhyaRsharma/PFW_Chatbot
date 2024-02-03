import os

from backend.services.db.conn import DB_FILE, get_cursor


def test_conn():
    cursor = get_cursor()
    cursor.execute("SELECT 1;")
    return True


def test_setup():
    cursor = get_cursor()
    result = cursor.execute("SELECT * from users LIMIT 2;")
    users = result.fetchall()
    result = cursor.execute("SELECT * from chats LIMIT 5;")
    chats = result.fetchall()
    return {"users": users, "chats": chats}


def setup_database():
    cur = get_cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            PASSWORD TEXT NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chats(
            id INTEGER PRIMARY KEY,
            user_id,
            query,
            response,
            accuracy,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )
    """)

    return True


def clear_database(resetup=True):
    os.remove(DB_FILE)

    if resetup:
        setup_database()

    return True


def execute_query(query):
    cursor = get_cursor()
    result = cursor.execute(query)
    return {"result": result.fetchall()}


def get_user_by_id(id):
    cursor = get_cursor()
    result = cursor.execute(f"SELECT id, name, email from users where id={id}")
    result = result.fetchone()

    if not result:
        return

    _, name, email = result
    return {'id': id, 'name': name, 'email': email}
