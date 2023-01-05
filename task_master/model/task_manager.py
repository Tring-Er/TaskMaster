"""Contains class TaskManager"""

from model.file_opener import create_file_opener


class TaskManager:
    """
    Manages tasks
    It's an interface on top of other objects
    """

    def __init__(self, tasks_file_path: str) -> None:
        self.__file_opener = create_file_opener(tasks_file_path)

    def add_task(self, task: str) -> None:
        """Adds a task to the tasks file and add a new line char at the end of the line

        Args:
            message (str): the task
        """

        self.__file_opener.add_task_to_file(task + "\n")

    def get_saved_tasks(self) -> str:
        """Return the tasks file content

        Args:
            tasks_file_path (str): The path of the tasks file

        Returns:
            str: The content of the file
        """

        return self.__file_opener.get_tasks_from_file()
