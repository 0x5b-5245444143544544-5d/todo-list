import sqlite3

# create a connection to the database, and creates a file if it doesn't exist yet.
c = sqlite3.connect('data.db')

def create_table() -> None:
    """ Creates table for use by the application. """
    
    query = '''CREATE TABLE IF NOT EXISTS tasks
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    TODO_CONTENT TEXT NOT NULL,
    IS_COMPLETE INTEGER NOT NULL DEFAULT FALSE);'''
    c.execute(query)
    c.commit()

def add_task(reminder_text: str) -> None:
    """ Adds a tasks to the database. """
    query = f'INSERT INTO tasks (TODO_CONTENT) values (\"{reminder_text}\");'
    c.execute(query)
    c.commit()

def get_tasks(is_complete: bool) -> list:
    """ Fetches incomplete tasks, optionally completed tasks. """
    query = f'SELECT * FROM tasks WHERE IS_COMPLETE={int(is_complete)};'
    cursor = c.execute(query)
    response = []
    for result in cursor:
        response.append({
            'id': result[0],
            'task_content': result[1],
            'is_complete': bool(result[2])
        })
    return response

def toggle_task(id: int) -> str:
    """ Toggle whether task is complete or not. """
    query = f"SELECT * FROM tasks WHERE ID={id};"
    cursor = list(c.execute(query))
    if not cursor:
        return "That task was not found.\n"
    is_complete = bool(cursor[0][2])
    query = f'''UPDATE tasks
    SET IS_COMPLETE={int(not is_complete)}
    WHERE id={id};
    '''
    c.execute(query)
    c.commit()
    return "Task state updated.\n"

def delete_task(id: int) -> str:
    """ Deletes a task. """
    query = f"SELECT * FROM tasks WHERE ID={id};"
    cursor = list(c.execute(query))
    if not cursor:
        return "That task was not found.\n"
    query = f"DELETE FROM tasks WHERE ID={id};"
    c.execute(query)
    c.commit()
    return "Task deleted.\n"

create_table()
