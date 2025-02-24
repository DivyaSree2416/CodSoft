todolist = []
def display_tasks():
    if len(todolist) == 0:
        print("Your To-Do list is empty.")
    else:
        for i in range(len(todolist)):
            status = "Done" if todolist[i][1] else "Not Done"
            print(f"{i+1}. {todolist[i][0]} - {status}")
def add_task():
    task = input("Enter a new task: ")
    todolist.append([task, False])  
def update_done():
    display_tasks()
    task_number = int(input("Enter the task number to update as done: "))
    if 1 <= task_number <= len(todolist):
        todolist[task_number - 1][1] = True
    else:
        print("Invalid task number.")
while True:
    print("\nTo-Do List Menu:")
    print("1. Display Tasks")
    print("2. Add a Task")
    print("3. Mark Task as Done")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")
