"""This module contains the class to read all tasks in the tasks file and all it's messages"""

from enum import Enum

from presenter.presenter import Presenter
from presenter.cli.modes.mode import Mode
from entities.Task import Task


class Messages(Enum):
    """Messages (string constants) used by the ReadTasks object"""


class ReadTasks(Mode):
    """This class execute the code to read all the tasks in the tasks file"""

    CLI_COMMAND = "read tasks"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        tasks_list = presenter.model.get_saved_tasks()
        tasks_formatted_string = ReadTasks.parse_tasks(tasks_list)
        presenter.view.print_message(tasks_formatted_string)
    
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
