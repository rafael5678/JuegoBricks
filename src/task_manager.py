class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)

    def complete_task(self):
        if not self.tasks:
            raise IndexError("No tasks to complete")
        return self.tasks.pop(0)