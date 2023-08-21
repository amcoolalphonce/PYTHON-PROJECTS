tasks = []
def display_tasks():
    if not tasks:
        print("No tasks in the to-do-list.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks, start = 1):
            print(f'{index}. {tasks}')

