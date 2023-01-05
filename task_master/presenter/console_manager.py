"""This class contains the presenter"""

from model.task_manager import TaskManager
from view.cli import CLI


TASK_FILE_PATH = r"C:\Altro\taskmaster\task_master\model\tasks.txt"


class ConsoleManager:
    """A presenter for a view and model"""

    @staticmethod
    def compute(model: TaskManager, view: CLI) -> None:
        """Make the program run

        Args:
            model (TaskManager): The TaskManager object
            view (CLI): The CLI object
        """

        view.print_message("Select mode (w/r)")
        mode = view.input_message()
        if mode == "w":
            view.print_message("Insert a task to save")
            message = view.input_message()
            model.add_task(TASK_FILE_PATH, message)
        elif mode == "r":
            file_content = model.get_saved_tasks(TASK_FILE_PATH)
            view.print_message(file_content)
        else:
            view.print_message(f"'{mode}' is not a valid mode!")
