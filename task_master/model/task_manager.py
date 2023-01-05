"""Contains class TaskManager"""

from model.file_opener import FileOpener


class TaskManager:
    """
    Manages tasks
    It's an interface on top of other objects
    """

    @staticmethod
    def add_task(tasks_file_path: str, task: str) -> None:
        """Adds a task to the tasks file and add a new line char at the end of the line

        Args:
            message (str): the task
        """

        FileOpener.add_task_to_file(tasks_file_path, task + "\n")
