# Simple To-Do List

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        num = int(input("Enter task number to update: "))
        if 0 < num <= len(tasks):
            tasks[num-1] = input("Enter new task: ")
            print("Task updated!")
        else:
            print("Invalid task number!")
    elif choice == "4":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid task number!")
    elif choice == "5":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice!")

