from data_access import TaskRepository


class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed


class TaskService:
    def __init__(self, repo=None):
        self.repo = repo if repo else TaskRepository()

    def add_task(self, task):
        self.repo.save_task(task)

    def get_all_tasks(self):
        return self.repo.get_tasks()

    def delete_task(self, index):
        tasks = self.repo.get_tasks()
        if 0 <= index < len(tasks):
            tasks.pop(index)
            self.repo.save_all_tasks(tasks)

    def mark_task_complete(self, index):
        tasks = self.repo.get_tasks()
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            self.repo.save_all_tasks(tasks)
