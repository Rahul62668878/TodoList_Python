import tkinter as tk
from tkinter import messagebox
import json

class TodiListGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")
        self.file_path = "todos.json"
        self.todos =self.load_todos()
        self.create_widgets()

    def load_todos(self):
        try:
            with open(self.file_path, "r") as file:
                task = json.load(file)
                return task
        except FileNotFoundError:
            return []
    
    def save_todos(self):
        with open(self.file_path, "w") as file:
            # file.write(str(self.todos))
            json.dump(self.todos, file, indent=4)

    def create_widgets(self):
        self.task_entry = tk.Entry(self.master, width=50,font=("Arial", 16))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.master,cursor="hand2 ",text="Add Task",width=20, font=("Arial", 16,'bold'),bg='green',fg='white', command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(self.master, width=50,borderwidth=4, relief="groove", font=("Arial", 16))
        self.task_listbox.pack(pady=10)

        self.populate_tasks()

        self.mark_button = tk.Button(self.master, text="Mark as Completed", command=self.mark_completed)
        self.mark_button.pack()

        self.delete_button = tk.Button(self.master,cursor="hand2 ",borderwidth=0 ,text="delete Task", border=3,width=20, font=("Arial", 16,'bold'),bg='green',fg='white', command=self.delete_task)
        self.delete_button.pack()

    def populate_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todos:
            status = "Completed" if task["completed"] else "Not Completed"
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todos.append({"task": task, "completed": False})
            self.save_todos()
            self.task_entry.delete(0, tk.END)
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            self.todos[idx]["completed"] = True
            self.save_todos()
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task.")
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            del self.todos[idx]
            self.save_todos()
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodiListGui(root)
    root.mainloop()