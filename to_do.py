todo = []

while True:

    print("TO DO LIST")
    print("1- Add Task")
    print("2- Show Tasks")
    print("3- Update Task")
    print("4- Delete Task")
    print("5- Clear All Tasks")
    print("6- Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        task = input("Enter a task: ")
        todo.append(task)
        print("Task added successfully.")

    elif option == 2:
        if len(todo) == 0:
            print("No tasks found.")
        else:
            for i in range(len(todo)):
                print(i + 1, "-", todo[i])

    elif option == 3:
        if len(todo) == 0:
            print("No tasks to update.")
        else:
            for i in range(len(todo)):
                print(i + 1, "-", todo[i])

            index = int(input("Enter task number: "))
            newTask = input("Enter the new task: ")
            todo[index - 1] = newTask
            print("Task updated successfully.")

    elif option == 4:
        if len(todo) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(todo)):
                print(i + 1, "-", todo[i])

            index = int(input("Enter task number: "))
            del todo[index - 1]
            print("Task deleted successfully.")

    elif option == 5:
        todo.clear()
        print("All tasks deleted.")

    elif option == 6:
        print("Good Bye!")
        break

    else:
        print("Invalid choice. Try again.")