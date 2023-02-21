"""This module contains the RemoveTask object and all messages used by it"""

from enum import Enum

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter
from entities.Task import Task


class Messages(Enum):
    """This class contains all messages (string constants) used by RemoveTask object"""

    SELECT_TASK_TO_REMOVE = "Select a task to remove"
    NO_NUMBER_FOUND = "No task found with that number"


class RemoveTask(Mode):
    """This class make possible to remove a task from the tasks file"""

    CLI_COMMAND = "remove task"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        tasks = presenter.model.get_saved_tasks()
        parsed_tasks = RemoveTask.parse_tasks(tasks)
        presenter.view.print_message(parsed_tasks)
        presenter.view.print_message(Messages.SELECT_TASK_TO_REMOVE.value)
        task_number_to_remove = presenter.view.input_message()
        task_index_to_remove = int(task_number_to_remove) - 1
        try:
            error = presenter.model.remove_task(tasks[task_index_to_remove])
        except IndexError:
            presenter.view.print_message(Messages.NO_NUMBER_FOUND.value)
    
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
