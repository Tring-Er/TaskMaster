"""This module contains the ExportTasks object and all messages used by it"""

from enum import StrEnum

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter


class Messages(StrEnum):
    """This class contains all messages (string constants) used by ExportTasks object"""

    TASKS_EXPORTED = "Tasks exported!"


class ExportTasks(Mode):
    """This class makes possible to export all tasks"""

    CLI_COMMAND = "export tasks"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.model.export_tasks()
        presenter.view.print_message(Messages.TASKS_EXPORTED)
