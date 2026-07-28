tasks_list = []

def add_task():
    while True:
        task = input("Enter your task (0 to stop): ")

        if task == "0":
            break

        tasks_list.append(task)

    print("Tasks added successfully.")


def read_task():
    if len(tasks_list) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks_list)):
            print(i + 1, "-", tasks_list[i])


def update_task():
    read_task()

    if len(tasks_list) == 0:
        return

    index = int(input("Enter task number: "))
    new_task = input("Enter new task: ")

    tasks_list[index - 1] = new_task

    print("Task updated successfully.")


def delete_task():
    read_task()

    if len(tasks_list) == 0:
        return

    index = int(input("Enter task number: "))

    del tasks_list[index - 1]

    print("Task deleted successfully.")


def clear_tasks():
    tasks_list.clear()
    print("All tasks deleted.")


def done_task():
    read_task()

    if len(tasks_list) == 0:
        return

    index = int(input("Enter task number: "))

    tasks_list[index - 1] = tasks_list[index - 1] + "DONE"

    print("Task marked as DONE.")


while True:

    print("TO DO LIST")
    print("1- Add Task")
    print("2- View Tasks")
    print("3- Update Task")
    print("4- Delete Task")
    print("5- Delete All Tasks")
    print("6- Mark Task as DONE")
    print("7- Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        add_task()

    elif choice == 2:
        read_task()

    elif choice == 3:
        update_task()

    elif choice == 4:
        delete_task()

    elif choice == 5:
        clear_tasks()

    elif choice == 6:
        done_task()

    elif choice == 7:
        print("Good Bye")
        break

    else:
        print("Invalid Choice.")