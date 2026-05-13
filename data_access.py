class TaskRepository:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def save_task(self, task):
        with open(self.filename, "a") as file:
            file.write(f"{task.title},{task.description},{task.completed}\n")

    def get_tasks(self):
        tasks = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    title, description, completed = line.strip().split(",")
                    tasks.append(
                        {
                            "title": title,
                            "description": description,
                            "completed": completed == "True",
                        }
                    )
        except FileNotFoundError:
            pass
        return tasks

    def save_all_tasks(self, tasks):
        with open(self.filename, "w") as file:
            for task in tasks:
                file.write(
                    f"{task['title']},{task['description']},{task['completed']}\n"
                )
