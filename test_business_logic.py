import unittest

from business_logic import TaskService, Task


class MockRepository:
    def __init__(self):
        self.tasks = []

    def save_task(self, task):
        self.tasks.append(
            {
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
            }
        )

    def get_tasks(self):
        return self.tasks

    def save_all_tasks(self, tasks):
        self.tasks = tasks


class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.repo = MockRepository()
        self.service = TaskService(self.repo)

    def test_add_task(self):
        task = Task("Homework", "Finish Python")
        self.service.add_task(task)
        self.assertEqual(len(self.repo.tasks), 1)

    def test_view_tasks(self):
        task = Task("Homework", "Finish Python")
        self.service.add_task(task)
        tasks = self.service.get_all_tasks()
        self.assertEqual(tasks[0]["title"], "Homework")

    def test_delete_task(self):
        task = Task("Homework", "Finish Python")
        self.service.add_task(task)
        self.service.delete_task(0)
        self.assertEqual(len(self.repo.tasks), 0)

    def test_mark_task_complete(self):
        task = Task("Homework", "Finish Python")
        self.service.add_task(task)
        self.service.mark_task_complete(0)
        self.assertTrue(self.repo.tasks[0]["completed"])


if __name__ == "__main__":
    unittest.main()
