import storage
import tkinter as tk
from tkinter import messagebox

def add_task(task_entry, listbox, all_tasks):
    task = task_entry.get()
    if task:
        all_tasks.append(task)
        storage.save_tasks(all_tasks)
        n = len(all_tasks)
        listbox.insert(tk.END, f'{n}. {task}')
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'You must enter a task to add')

def update_task(task_entry, listbox, all_tasks):
    index_tpl = listbox.curselection()
    if index_tpl:
        n = index_tpl[0]
        modified_task = task_entry.get()
        all_tasks[n] = modified_task
        storage.save_tasks(all_tasks)
        listbox.delete(n)
        listbox.insert(n, f'{n+1}. {modified_task}')
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'You must choose a task to update')

def remove_task(task_entry, listbox, all_tasks):
    index_tpl = listbox.curselection()
    if index_tpl:
        n = index_tpl[0]
        del all_tasks[n]
        storage.save_tasks(all_tasks)
        listbox.delete(0, tk.END)
        for i, item in enumerate(all_tasks):
            listbox.insert(tk.END, f'{i+1}. {item}')
    else:
        messagebox.showwarning('Warning', 'You must choose a task to remove')

def confirm_exit(root):
    if messagebox.askokcancel('Exit', 'Do you want to exit the program?'):
        root.destroy()