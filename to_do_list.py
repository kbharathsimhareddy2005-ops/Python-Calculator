todo_list = []

def add():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully.")

def view():
    if len(todo_list) == 0:
        print("List is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove():
    if len(todo_list) == 0:
        print("List is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

        try:
            num = int(input("Enter the task number to remove: "))

            if 1 <= num <= len(todo_list):
                removed_task = todo_list.pop(num - 1)
                print(f"{removed_task} removed successfully.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        add()

    elif choice == 2:
        view()

    elif choice == 3:
        remove()

    elif choice == 4:
        print("Exited successfully.")
        break

    else:
        print("Please enter a number between 1 and 4.")