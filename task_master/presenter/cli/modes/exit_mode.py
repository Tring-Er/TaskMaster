"""The exit mode quits the program, this module contains messages used by ExitMode"""

from enum import Enum
from sys import exit as sys_exit

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter


class Messages(Enum):
    """Messages (strings contants) used by ExitMode"""

    EXIT_MESSAGE = "Quitting the program..."


class ExitMode(Mode):
    """Exits the program"""

    CLI_COMMAND = "exit"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.print_message(Messages.EXIT_MESSAGE.value)
        sys_exit(0)
