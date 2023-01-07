"""This module contains the class to read all tasks in the tasks file and all it's messages"""

from enum import StrEnum

from presenter.presenter import Presenter
from presenter.modes.mode import Mode


class Messages(StrEnum):
    """Messages (string constants) used by the ReadTasks object"""


class ReadTasks(Mode):
    """This class execute the code to read all the tasks in the tasks file"""

    CLI_COMMAND = "read tasks"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        tasks_list = presenter.model.get_saved_tasks()
        tasks_formatted_string = presenter.model.parse_tasks(tasks_list)
        presenter.view.print_message(tasks_formatted_string)
