"""This class contains the presenter and messages (strings constants) used by the presenter"""

from enum import Enum

from presenter.presenter import Presenter
from presenter.cli.modes import MODES, Mode


class Messages(Enum):
    """All Messages used by console_manager"""

    CHOOSE_MODE = "Select mode ({})"


class ConsoleManager(Presenter):
    """A presenter for a view and model"""
    
    def print_message(self, message: str) -> None:
        """It prints the message on the console

        Args:
            message (str): the message to print
        """
        print(message)

    def input_message(self) -> str:
        """Return the input passed in the console

        Returns:
            str: The string inserted by user
        """
        return input()

    def get_modes_simbols(self) -> str:
        """Returns all the MODES symbols (the string paired with the mode) excluding the InvalidMode

        Returns:
            str: The string contaning all the symbols
            it follows this pattern: "symbol_1/symbol_2/.../symbol_n"
        """

        modes_symbols = list(MODES.keys())
        modes_symbols.remove("")
        modes_symbols_excluded_invalid = "/".join(modes_symbols)
        return modes_symbols_excluded_invalid

    def compute(self) -> None:
        """Make the program run"""

        modes_symbols = self.get_modes_simbols()
        while True:
            self.print_message(Messages.CHOOSE_MODE.value.format(modes_symbols))
            input_mode = self.input_message()
            selected_mode: Mode = MODES.get(input_mode, MODES[""])
            selected_mode.execute(self)
