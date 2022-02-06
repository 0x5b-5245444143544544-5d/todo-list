from utils import database

def add_task():
    task = input("\nEnter task particulars: ")
    database.add_task(task)
    print("Task added.\n\n")

def modify_incomplete_tasks():
    """ TODO """

def modify_complete_tasks():
    """ TODO """

choices = {
    'a': add_task,
    'b': modify_incomplete_tasks,
    'c': modify_complete_tasks
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
