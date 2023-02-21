"""Contains class TaskManager"""

from model.file_opener import create_file_manager

from entities.Task import Task
from use_cases.TasksManager import TasksManager as _TaskManager


class TaskManager:
    """
    Manages tasks
    It's an interface on top of other objects
    """

    def __init__(self) -> None:
        self.__file_opener = create_file_manager()

    def add_task(self, task: Task) -> None:
        """Adds a task to the tasks file

        Args:
            task (Task): the task object
        """

        _TaskManager.add_task(self.__file_opener, task)

    def get_saved_tasks(self) -> list[Task]:
        """Return the tasks saved in the tasks file

        Returns:
            list[Task]: The tasks on the task file
        """

        return _TaskManager.read_tasks(self.__file_opener)

    def remove_task(self, task_index: int) -> None | Exception:
        """Removes a task from the tasks file

        Args:
            task_index (int): The index of the task

        Returns:
            None | Exception: Returns an Exeption if the index is out of range
        """

        tasks = self.__file_opener.read()
        if not 0 <= task_index <= len(tasks) - 1:
            return IndexError()
        tasks.pop(task_index)
        self.__file_opener.overwrite_tasks(tasks)

    def parse_tasks(self, tasks: list[Task]) -> str:
        """It returns a string with this pattern:
        '{task_index}- {task}\\n\\n{task_index}- {task}\\n\\n...{task_index}- {task}\\n\\n'

        Args:
            tasks (list[str]): The tasks to put in the string

        Returns:
            str: The string with the pattern written above
        """

        string_to_return = ""
        for task_number, task in enumerate(tasks, 1):
            string_to_return += f"{task_number}- {task.text}\n"
        return string_to_return

    def export_tasks(self) -> None:
        """Exports tasks into the same directory"""

        self.__file_opener.export_tasks()

    def change_task_position(self,
                             tasks: list[str],
                             task_position: str,
                             new_task_position: str
                             ) -> None:
        """Change the position of a task into the selected position

        Args:
            tasks (list[str]): the tasks list
            task_position (int): task's position
            new_task_position (int): task's new position
        """

        task_index = int(task_position) - 1
        new_task_index = int(new_task_position) - 1
        tasks[task_index], tasks[new_task_index] = tasks[new_task_index], tasks[task_index]
        self.__file_opener.overwrite_tasks(tasks)
