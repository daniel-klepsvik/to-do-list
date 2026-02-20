import json

FILENAME = 'tasks.json'

def load_tasks():
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)