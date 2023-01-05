"""This class contains the presenter"""

from typing import Type

from model.task_manager import TaskManager
from view.cli import CLI


TASK_FILE_PATH = r"C:\Altro\taskmaster\task_master\model\tasks.txt"


class ConsoleManager:
    """A presenter for a view and model"""

    def __init__(self, model: Type[TaskManager], view: Type[CLI]) -> None:
        self.model = model(TASK_FILE_PATH)
        self.view = view()

    def compute(self) -> None:
        """Make the program run

        Args:
            model (TaskManager): The TaskManager object
            view (CLI): The CLI object
        """

        self.view.print_message("Select mode (w/r)")
        mode = self.view.input_message()
        if mode == "w":
            self.view.print_message("Insert a task to save")
            message = self.view.input_message()
            self.model.add_task(message)
        elif mode == "r":
            file_content = self.model.get_saved_tasks()
            self.view.print_message(file_content)
        else:
            self.view.print_message(f"'{mode}' is not a valid mode!")
