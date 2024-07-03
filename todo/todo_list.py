import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = {
            'id': self.next_id,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def view_tasks(self):
        return self.tasks

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                return task
        return None

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                return task
        return None

class ToDoApp:
    def __init__(self, root):
        self.to_do_list = ToDoList()
        self.root = root
        self.root.title("To-Do List Application")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.tasks_listbox = tk.Listbox(self.frame, width=60, height=15)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        self.complete_button = tk.Button(self.frame, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=5, pady=5)

    def add_task(self):
        description = self.task_entry.get()
        if description:
            task = self.to_do_list.add_task(description)
            self.tasks_listbox.insert(tk.END, f"{task['id']}. {task['description']} (Pending)")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task description.")

    def update_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            task_id = int(self.tasks_listbox.get(selected_task_index).split('.')[0])
            new_description = self.task_entry.get()
            if new_description:
                task = self.to_do_list.update_task(task_id, new_description)
                self.tasks_listbox.delete(selected_task_index)
                self.tasks_listbox.insert(selected_task_index, f"{task['id']}. {task['description']} (Pending)")
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task description.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def complete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            task_id = int(self.tasks_listbox.get(selected_task_index).split('.')[0])
            task = self.to_do_list.complete_task(task_id)
            self.tasks_listbox.delete(selected_task_index)
            self.tasks_listbox.insert(selected_task_index, f"{task['id']}. {task['description']} (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            task_id = int(self.tasks_listbox.get(selected_task_index).split('.')[0])
            self.to_do_list.delete_task(task_id)
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
