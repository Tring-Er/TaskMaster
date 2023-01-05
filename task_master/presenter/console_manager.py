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

        tasks_file_path = r"C:\Altro\taskmaster\task_master\model\tasks.txt"
        message = view.input_message()
        model.add_task(tasks_file_path, message)
