"""This module contains the class to execute the code in case of invalid mode"""

from presenter.presenter import Presenter
from presenter.modes.mode import Mode


class InvalidMode(Mode):
    """Run the code in case of invalid mode"""

    CLI_COMMAND = ""

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.view.print_message("The input inserted was not a valid mode!")
