"""This class contains the presenter"""

from model.task_manager import TaskManager
from view.cli import CLI


class ConsoleManager:
    """A presenter for a view and model"""

    @staticmethod
    def compute(model: TaskManager, view: CLI) -> None:
        """Make the program run

        Args:
            model (TaskManager): The TaskManager object
            view (CLI): The CLI object
        """

        message = view.input_message()
        model_message = model.task(message)
        view.print_message(model_message)
