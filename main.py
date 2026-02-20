import storage
import logic
import tkinter as tk
from tkinter import messagebox

all_tasks = storage.load_tasks()

root = tk.Tk()
root.title('Task Manager')
root.geometry('400x400')
try:
    root.iconbitmap('task-manager.ico')
except Exception as e:
    print(f'Icon not found: {e}')

task_entry = tk.Entry(root, width=40, )
task_entry.pack(pady=10)

add_btn = tk.Button(root, text='Add Task', command=lambda: logic.add_task(task_entry, listbox, all_tasks))
add_btn.pack()
root.bind('<Return>', lambda event: logic.add_task(task_entry, listbox, all_tasks))
update_btn = tk.Button(root, text='Update Task', command=lambda: logic.update_task(task_entry, listbox, all_tasks))
update_btn.pack()
remove_btn = tk.Button(root, text='Remove Task', command=lambda: logic.remove_task(task_entry, listbox, all_tasks))
remove_btn.pack()
exit_btn = tk.Button(root, text='Exit', command=lambda: logic.confirm_exit(root))
exit_btn.pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

for i, item in enumerate(all_tasks):
    listbox.insert(tk.END, f'{i+1}. {item}')

root.mainloop()