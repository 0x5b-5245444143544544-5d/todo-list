from utils import database
from beautifultable import BeautifulTable

def add_task():
    task = input("\nEnter task particulars: ")
    database.add_task(task)
    print("Task added.\n\n")

def modify_incomplete_tasks():
    """ TODO """
    table = BeautifulTable()
    table.columns.header = ["ID", "Task Particulars"]
    tasks = database.get_tasks(is_complete=False)
    if not tasks:
        print("\nThere are no incomplete tasks.\n")
        return
    for task in tasks:
        table.rows.append([task['id'], task['task_content']])
    print(table)
    print()
    
    choice = input("Toggle task state(c), delete task(d) or back to menu(any other key): ")
    if not choice:
        return
    choice = choice[0].lower()
    if choice not in choices_menu_2.keys():
        return
    choices_menu_2[choice]()

def modify_complete_tasks():
    """ TODO """
    table = BeautifulTable()
    table.columns.header = ["ID", "Task Particulars"]
    tasks = database.get_tasks(is_complete=True)
    if not tasks:
        print("\nThere are no complete tasks.\n")
        return
    for task in tasks:
        table.rows.append([task['id'], task['task_content']])
    print(table)
    print()

    choice = input("Toggle task state(c), delete task(d) or back to menu(any other key): ")
    if not choice:
        return
    choice = choice[0].lower()
    if choice not in choices_menu_2.keys():
        return
    choices_menu_2[choice]()

def toggle_task():
    id = input("Enter task ID to toggle: ")
    if not id.isnumeric():
        print("Invalid task ID.")
        return
    id = int(id)
    print(database.toggle_task(id))

def delete_task():
    id = input("Enter task ID to delete: ")
    if not id.isnumeric():
        print("Invalid task ID.")
        return
    id = int(id)
    print(database.delete_task(id))

choices = {
    'a': add_task,
    'b': modify_incomplete_tasks,
    'c': modify_complete_tasks
}

choices_menu_2 = {
    'c': toggle_task,
    'd': delete_task
}

while True:
    print("Menu")
    print("a. Add a task")
    print("b. List and modify incomplete tasks")
    print("c. List and modify complete tasks")
    choice = input("Enter a choice (invalid choice quits): ")
    if not choice:
        print("Please try again.")
        continue
    choice = choice[0].lower()
    if not choice in choices.keys():
        print("Quitting!")
        break

    choices[choice]()
