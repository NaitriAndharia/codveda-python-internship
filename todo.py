
import json
import os

FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


# Save tasks in JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


# Add new task
def add_task():
    task = input("Enter your task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


# View all tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")

        for i, task in enumerate(tasks, start=1):
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(i, ".", task["task"], "-", status)


# Delete a task
def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print("Task deleted:", removed["task"])
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Mark task as completed
def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_no = int(input("Enter task number to complete: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as Completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def main():
    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            print("Thank you for using To-Do List Application!")
            break

        else:
            print("Invalid choice! Please enter 1 to 5.")


# Start application
main()
