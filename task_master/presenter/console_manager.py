"""This class contains the presenter"""

from model.task_manager import TaskManager
from presenter.presenter import Presenter
from presenter.modes import MODES, Mode
from view.cli import CLI


class ConsoleManager(Presenter):
    """A presenter for a view and model"""

    def __init__(self, model: TaskManager, view: CLI) -> None:
        self.model = model
        self.view = view

    def compute(self) -> None:
        """Make the program run

        Args:
            model (TaskManager): The TaskManager object
            view (CLI): The CLI object
        """

        self.view.print_message("Select mode (w/r)")
        input_mode = self.view.input_message()
        selected_mode: Mode = MODES.get(input_mode, MODES[""])
        selected_mode.execute(self)
