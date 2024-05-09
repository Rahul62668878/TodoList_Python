import json


class TodoList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.todos = self.load_todos()

    def load_todos(self):
        try:
            with open(self.file_path, "r") as file:
                # todos= eval(file.read())
                todos = json.load(file)
                return todos
        except FileNotFoundError:
            return []

    def save_todos(self):
        with open(self.file_path, "w") as file:
            # file.write(str(self.todos))
            json.dump(self.todos, file, indent=4)

    def delete_all(self):
        confirm = input('Are you sure you want to delete all todos? (y/n): ')
        if confirm == 'y':
            self.todos = []
            self.save_todos()
        else:
            print('Deletion cancelled')
            return
        # with open(self.file_path, "w") as file:
        #     file.write("[]")
        #     print('all todos are deleted')

    def addTodo(self):
        task = input("Enter Todo: ")
        self.todos.append({"task": task, "completed": False})
        self.save_todos()
        print("task added successfully")

    def removeTodo(self):
        self.getTodos()
        task_number = int(input("Enter task number: "))
        if 1 <= task_number <= len(self.todos):
            del self.todos[task_number - 1]
            self.save_todos()
            print("Task deleted successfully")
        else:
            print("Invalid task number")

    def getTodos(self):
        if not self.todos:
            print("No todos found")
        # print("\nTodos:")
        for idx, todo in enumerate(self.todos, start=1):
            status = "Completed" if todo["completed"] else "Not Completed"
            print(f"{idx}.{todo['task']}-{status}")
        # return self.todos

    def mark_as_complete(self):
        self.getTodos()
        task_number = int(input("Enter task number: "))
        if 1 <= task_number <= len(self.todos):
            self.todos[task_number - 1]["completed"] = True
            self.save_todos()
            print("Task marked as completed successfully")
        else:
            print("Invalid task number")

    def show_menu(self):
        print("\n===== Todo List =====")
        print("1. Add Todo")
        print("2. View Todos")
        print("3", "Mark as completed")
        print("4. Delete Todo")
        print("5. Delete All")
        print("6. Exit")
        print("===== Todo List End =====")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addTodo()
            elif choice == "2":
                self.getTodos()
            elif choice == "3":
                self.mark_as_complete()
            elif choice == "4":
                self.removeTodo()
            elif choice == "5":
               self.delete_all()
            elif choice == "6":
                break
            else:
                print("Invalid choice please enter a number a between 1 and 5")


if __name__ == "__main__":
    todo_list = TodoList("todos.txt")
    todo_list.run()
