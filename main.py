import json
import storage

tasks = storage.load_tasks()
storage.view_tasks(tasks)
while True:
    print('\n--- Main Menu ---')
    print('Add, View, Remove, and Exit')
    option = input('What do you want to do? ')
    if option.lower() == 'add':
        new_task = input('New Task: ')
        tasks.append(new_task)
        storage.save_tasks(tasks)
        print('Task Successfully Added')
    elif option.lower() == 'view':
        storage.view_tasks(tasks)
    elif option.lower() == 'remove':
        while True:
            n = input('Which task do you want to remove? ')
            try:
                n = int(n)
                if 0 < n <= len(tasks):
                    tasks.pop(n-1)
                    storage.save_tasks(tasks)
                    print('Task Successfully Removed')
                    break
                else:
                    print('Invalid Task Number')
                    choice_1 = input('Do you want to view the list again? (Yes/No) ')
                    if choice_1 == 'yes':
                        storage.view_tasks(tasks)
                    else:
                        choice_2 = input('Do you want to return to the Main Menu? (Yes/No) ')
                        if choice_2.lower() == 'yes':
                            break
            except ValueError:
                print('Invalid Task Number')
                choice_1 = input('Do you want to view the list again? (Yes/No) ')
                if choice_1 == 'yes':
                    storage.view_tasks(tasks)
                else:
                    choice_2 = input('Do you want to return to the Main Menu? (Yes/No) ')
                    if choice_2.lower() == 'yes':
                        break
    elif option.lower() == 'exit':
        print('Exited Program')
        break
    else:
        print('Invalid Input')