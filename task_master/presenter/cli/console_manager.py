"""This class contains the presenter and messages (strings constants) used by the presenter"""

from enum import Enum

from model.task_manager import TaskManager
from presenter.presenter import Presenter
from presenter.cli.modes import MODES, Mode
from view.cli import CLI


class Messages(Enum):
    """All Messages used by console_manager"""

    CHOOSE_MODE = "Select mode ({})"


class ConsoleManager(Presenter):
    """A presenter for a view and model"""

    def __init__(self, model: TaskManager, view: CLI) -> None:
        self.model = model
        self.view = view

    @staticmethod
    def __get_modes_simbols() -> str:
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

        modes_symbols = self.__get_modes_simbols()
        while True:
            self.view.print_message(Messages.CHOOSE_MODE.value.format(modes_symbols))
            input_mode = self.view.input_message()
            selected_mode: Mode = MODES.get(input_mode, MODES[""])
            selected_mode.execute(self)
