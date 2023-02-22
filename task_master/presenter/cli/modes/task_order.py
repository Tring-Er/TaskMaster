"""This module contains the TaskOrder object and all messages used by it"""

from enum import Enum

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter
from entities.Task import Task
from use_cases.TasksManager import TasksManager
from details.TextFile import TextFile


class Messages(Enum):
    """This class contains all messages (string constants) used by TaskOrder object"""

    SELECT_TASK_TO_MOVE = "Select a task to change position"
    SELECT_POSITION = "Select the position to move the task to"


class TaskOrder(Mode):
    """This class makes possible to change a task order"""

    CLI_COMMAND = "task order"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        file_manager = TextFile()
        tasks = TasksManager.read_tasks(file_manager)
        parsed_tasks = TaskOrder.parse_tasks(tasks)
        presenter.print_message(parsed_tasks)
        presenter.print_message(Messages.SELECT_TASK_TO_MOVE.value)
        old_task_index = int(presenter.input_message()) - 1
        presenter.print_message(Messages.SELECT_POSITION.value)
        new_task_index = int(presenter.input_message()) - 1
        TasksManager.change_oder(old_task_index, new_task_index, file_manager)
    
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
