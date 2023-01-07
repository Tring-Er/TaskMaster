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

    def get_saved_tasks(self) -> list[str]:
        """Return the tasks file content

        Args:
            tasks_file_path (str): The path of the tasks file

        Returns:
            str: The content of the file
        """

        return self.__file_opener.get_tasks_from_file()

    def remove_task(self, task_index: int) -> None:
        """Removes a task from the tasks file

        Args:
            task_index (int): The index of the task
        """

        tasks = self.__file_opener.get_tasks_from_file()
        tasks.pop(task_index)
        self.__file_opener.overwrite_tasks_file(tasks)

    def parse_tasks(self, tasks: list[str]) -> str:
        """It returns a string with this pattern:
        '{task_index}- {task}\n\n{task_index}- {task}\n\n...{task_index}- {task}\n\n'

        Args:
            tasks (list[str]): The tasks to put in the string

        Returns:
            str: The string with the pattern written above
        """

        string_to_return = ""
        for task_number, task in enumerate(tasks, 1):
            string_to_return += f"{task_number}- {task}\n"
        return string_to_return
