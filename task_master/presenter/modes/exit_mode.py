"""The exit mode quits the program, this module contains messages used by ExitMode"""

from enum import StrEnum
from sys import exit as sys_exit

from presenter.modes.mode import Mode
from presenter.presenter import Presenter


class Messages(StrEnum):
    """Messages (strings contants) used by ExitMode"""

    EXIT_MESSAGE = "Quitting the program..."


class ExitMode(Mode):
    """Exits the program"""

    CLI_COMMAND = "e"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.view.print_message(Messages.EXIT_MESSAGE)
        sys_exit(0)
