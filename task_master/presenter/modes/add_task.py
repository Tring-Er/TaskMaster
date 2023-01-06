"""This module contains the an object that adds a task to the tasks file and all it's messages
used
"""

from enum import StrEnum

from presenter.modes.mode import Mode
from presenter.presenter import Presenter


class Messages(StrEnum):
    """Messages (string constants) used by the AddTask object"""

    ASK_FOR_TASK = "Insert a task to save"


class AddTask(Mode):
    """This class execute the code to add a task to the tasks file"""

    CLI_COMMAND = "w"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.view.print_message(Messages.ASK_FOR_TASK)
        message = presenter.view.input_message()
        presenter.model.add_task(message)
