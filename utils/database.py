import sqlite3

# create a connection to the database, and creates a file if it doesn't exist yet.
c = sqlite3.connect('data.db')

def create_table() -> None:
    """ Creates table for use by the application. """
    query = '''CREATE TABLE tasks
    (ID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    TODO_CONTENT TEXT NOT NULL,
    IS_COMPLETE INTEGER NOT NULL DEFAULT FALSE);'''
    c.execute(query)
    c.commit()

def add_reminder(reminder_text: str) -> None:
    """ Adds a reminder to the database. """
    query = f'INSERT INTO tasks (TODO_CONTENT) values ({reminder_text});'
    c.execute(query)
    c.commit()

def get_reminder(id: int, is_complete: bool = False) -> list:
    """ Fetches incomplete reminders, optionally completed reminders. """
    query = f'SELECT * FROM tasks WHERE id={id} AND IS_COMPLETE={int(is_complete)};'
    cursor = c.execute()
    response = []
    for result in cursor:
        response.append({
            'id': result['ID'],
            'reminder_content': result['TODO_CONTENT'],
            'is_complete': bool(result['IS_COMPLETE'])
        })
    return response


create_table()
