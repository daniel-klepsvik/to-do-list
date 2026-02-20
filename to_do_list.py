tasks = []
while True:
    print('Add, View, Remove, and Exit')
    option = input('What do you want to do? ')
    if option.lower() == 'add':
        new_task = input('New Task: ')
        tasks.append(new_task)
        print('Task Successfully Added')
    elif option.lower() == 'view':
        if tasks == []:
            print('No Tasks Found')
        else:
            for i, task in enumerate(tasks, start=1):
                print(f'{i}: {task}')
    elif option.lower() == 'remove':
        while True:
            n = input('Which task do you want to remove? ')
            try:
                n = int(n)
                if 0 < n <= len(tasks):
                    tasks.pop(n-1)
                    print('Task Successfully Removed')
                    break
                else:
                    print('Invalid Task Number')
                    choice = input('Do you want to return to the Main Menu? (Yes/No) ')
                    if choice.lower() == 'yes':
                        break
            except ValueError:
                print('Invalid Task Number')
                choice = input('Do you want to return to the Main Menu? (Yes/No) ')
                if choice.lower() == 'yes':
                    break
    elif option.lower() == 'exit':
        print('Exited Program')
        break
    else:
        print('Invalid Input')