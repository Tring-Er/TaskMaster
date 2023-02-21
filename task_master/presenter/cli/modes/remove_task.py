"""This module contains the RemoveTask object and all messages used by it"""

from enum import Enum

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter
from entities.Task import Task
from use_cases.TasksManager import TasksManager
from model.file_opener import FileManager


class Messages(Enum):
    """This class contains all messages (string constants) used by RemoveTask object"""

    SELECT_TASK_TO_REMOVE = "Select a task to remove"
    NO_NUMBER_FOUND = "No task found with that number"


class RemoveTask(Mode):
    """This class make possible to remove a task from the tasks file"""

    CLI_COMMAND = "remove task"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        file_manager = FileManager()
        tasks = TasksManager.read_tasks(file_manager)
        parsed_tasks = RemoveTask.parse_tasks(tasks)
        presenter.print_message(parsed_tasks)
        presenter.print_message(Messages.SELECT_TASK_TO_REMOVE.value)
        task_number_to_remove = presenter.input_message()
        task_index_to_remove = int(task_number_to_remove) - 1
        try:
            TasksManager.remove_task(tasks[task_index_to_remove], file_manager)
        except IndexError:
            presenter.print_message(Messages.NO_NUMBER_FOUND.value)
    
    @staticmethod
    def parse_tasks(tasks: list[Task]) -> str:
        """It returns a string with this pattern:
        '{task_index}- {task}\\n\\n{task_index}- {task}\\n\\n...{task_index}- {task}\\n\\n'

        Args:
            tasks (list[Task]): The tasks to put in the string

        Returns:
            str: The string with the pattern written above
        """

        string_to_return = ""
        for task_number, task in enumerate(tasks, 1):
            string_to_return += f"{task_number}- {task.text}\n"
        return string_to_return
