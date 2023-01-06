"""This module contains the class to execute the code in case of invalid mode and
all messages used by it
"""

from enum import StrEnum

from presenter.presenter import Presenter
from presenter.modes.mode import Mode


class Messages(StrEnum):
    """Messages (string constants) used by the InvalidMode object"""

    INVALID_MODE_SELECTED = "The input inserted was not a valid mode!"


class InvalidMode(Mode):
    """Run the code in case of invalid mode"""

    CLI_COMMAND = ""

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.view.print_message(Messages.INVALID_MODE_SELECTED)
