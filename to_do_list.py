tasks = []
def display_tasks():
    if not tasks:
        print("No tasks in the to-do-list.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks, start = 1):
            print(f'{index}. {tasks}')

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")