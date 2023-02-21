"""Contains class TaskManager"""

from model.file_opener import create_file_manager

from entities.Task import Task
from use_cases.TasksManager import TasksManager as _TaskManager


class TaskManager:
    """
    Manages tasks
    It's an interface on top of other objects

    THIS OBJECT WILL BE DEPRECATED AND REMOVED SOON
    """

    def __init__(self) -> None:
        self.__file_opener = create_file_manager()

    def add_task(self, task: Task) -> None:
        """Adds a task to the tasks file

        Args:
            task (Task): the task object
        """

        _TaskManager.add_task(task, self.__file_opener)

    def get_saved_tasks(self) -> list[Task]:
        """Return the tasks saved in the tasks file

        Returns:
            list[Task]: The tasks on the task file
        """

        return _TaskManager.read_tasks(self.__file_opener)

    def remove_task(self, task: Task) -> None:
        """Removes a task from the tasks file

        Args:
            task (Task): The task to remove
        """

        _TaskManager.remove_task(task, self.__file_opener)

    def change_task_position(self, task_index: int, new_task_index: int) -> None:
        """Change the position of a task to the selected position

        Args:
            task_position (int): task's position
            new_task_position (int): task's new position
        """

        _TaskManager.change_oder(task_index, new_task_index, self.__file_opener)
