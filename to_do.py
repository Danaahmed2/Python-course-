tasks = []

while True:
    print("TO DO LIST ")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Delete All Tasks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == 3:
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        num = int(input("Enter task number: "))
        new_task = input("Enter new task: ")
        tasks[num - 1] = new_task

    elif choice == 4:
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        num = int(input("Enter task number: "))
        del tasks[num - 1]

    elif choice == 5:
        tasks.clear()
        print("All tasks deleted.")

    elif choice == 6:
        print("Good Bye")
        break

    else:
        print("Invalid Choice")