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

    @staticmethod
    def get_saved_tasks(tasks_file_path: str) -> str:
        """Return the tasks file content

        Args:
            tasks_file_path (str): The path of the tasks file

        Returns:
            str: The content of the file
        """

        return FileOpener.get_tasks_from_file(tasks_file_path)
