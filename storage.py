import json

def save_tasks(tasks):
    with open('to_do_list.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    if not tasks:
        print('Your list is empty')
    else:
        print('\nTo-Do List')
        for i, task in enumerate(tasks, start=1):
            print(f'{i}: {task}')