import os
from datetime import datetime


def task_format(task, category):
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return f"[{category}] {task} (Added on: {date_time})"

def task_load(listbox):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert("end", task.strip())

def task_save(listbox):
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in listbox.get(0, "end"):
            file.write(task + "\n")