import tkinter as tk
from tkinter import messagebox
from tasks import task_load, task_save

def add_tasks():
    tasks = entry.get().strip()
    category = category_var.get()

    if tasks == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    
    text_task = tasks_format(tasks, category)
    
    if text_task in listbox.get(0, tk.END):
        messagebox.showwarning("Warning", "Task already exists!")
        return
    
    listbox.insert(tk.END, text_task)
    entry.delete(0, tk.END)
    task_save(listbox)

def delete_tasks():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        task_save(listbox)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def tasks_format(task, category):
        return f"[{category}] {task}"

def mark_task_completed():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if not task.startswith("[Completed]"):
            listbox.delete(selected)
            listbox.insert(selected, f"[Completed] {task}")
            task_save(listbox)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def unmark_task_completed():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if task.startswith("[Completed]"):
            new_task = task.replace("[Completed] ", "", 1)
        else:
            new_task = f"[Completed] {task}"
        listbox.delete(selected)
        listbox.insert(selected, new_task)
        task_save(listbox)

    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

window = tk.Tk()
window.title("To-Do List")
window.geometry("500x500")
window.resizable(False, False)

heading = tk.Label(window, text="To-Do List", font=("Arial", 20, "bold"))
heading.pack(pady=10)

category_var = tk.StringVar(value="Work")
menu = tk.OptionMenu(window, category_var, "Work", "Personal", "Project","Study","Others")
menu.pack(pady=5)

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

listbox = tk.Listbox(window, width=55, height=15, font=("Arial", 12))
listbox.pack(pady=10)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Task", command=add_tasks, width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete Task", command=delete_tasks,width=10).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Mark Completed", command=mark_task_completed,width=15).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Unmark Completed", command=unmark_task_completed,width=15).grid(row=0, column=3, padx=5)

task_load(listbox)

window.mainloop()