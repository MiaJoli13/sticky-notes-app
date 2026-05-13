from business_logic import TaskService, Task


def start_application():
    service = TaskService()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter title: ")
            desc = input("Enter description: ")
            service.add_task(Task(title, desc))
            print("Task added!")
        elif choice == "2":
            tasks = service.get_all_tasks()
            for i, task in enumerate(tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['title']} - {task['description']} - {status}")
        elif choice == "3":
            index = int(input("Enter task number: "))
            service.mark_task_complete(index)
            print("Task marked complete")
        elif choice == "4":
            index = int(input("Enter task number: "))
            service.delete_task(index)
            print("Task deleted")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    start_application()
