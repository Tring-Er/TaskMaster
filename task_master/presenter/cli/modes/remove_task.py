"""This module contains the RemoveTask object and all messages used by it"""

from enum import Enum

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter


class Messages(Enum):
    """This class contains all messages (string constants) used by RemoveTask object"""

    SELECT_TASK_TO_REMOVE = "Select a task to remove"
    NO_NUMBER_FOUND = "No task found with that number"


class RemoveTask(Mode):
    """This class make possible to remove a task from the tasks file"""

    CLI_COMMAND = "remove task"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        tasks = presenter.model.get_saved_tasks()
        parsed_tasks = presenter.model.parse_tasks(tasks)
        presenter.view.print_message(parsed_tasks)
        presenter.view.print_message(Messages.SELECT_TASK_TO_REMOVE.value)
        task_number_to_remove = presenter.view.input_message()
        task_index_to_remove = int(task_number_to_remove) - 1
        error = presenter.model.remove_task(task_index_to_remove)
        if isinstance(error, IndexError):
            presenter.view.print_message(Messages.NO_NUMBER_FOUND.value)
