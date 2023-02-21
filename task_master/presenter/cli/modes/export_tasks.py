"""This module contains the ExportTasks object and all messages used by it"""

from enum import Enum

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter
from model.file_opener import FileManager


class Messages(Enum):
    """This class contains all messages (string constants) used by ExportTasks object"""

    TASKS_EXPORTED = "Tasks exported!"


class ExportTasks(Mode):
    """This class makes possible to export all tasks"""

    CLI_COMMAND = "export tasks"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        file_manager = FileManager()
        file_manager.export_tasks()
        presenter.print_message(Messages.TASKS_EXPORTED.value)
