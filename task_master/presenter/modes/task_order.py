"""This module contains the TaskOrder object and all messages used by it"""

from enum import StrEnum

from presenter.modes.mode import Mode
from presenter.presenter import Presenter


class Messages(StrEnum):
    """This class contains all messages (string constants) used by TaskOrder object"""

    SELECT_TASK_TO_MOVE = "Select a task to change position"
    SELECT_POSITION = "Select the position to move the task to"


class TaskOrder(Mode):
    """This class makes possible to change a task order"""

    CLI_COMMAND = "task order"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        tasks = presenter.model.get_saved_tasks()
        parsed_tasks = presenter.model.parse_tasks(tasks)
        presenter.view.print_message(parsed_tasks)
        presenter.view.print_message(Messages.SELECT_TASK_TO_MOVE)
        old_task_position = presenter.view.input_message()
        presenter.view.print_message(Messages.SELECT_POSITION)
        new_task_position = presenter.view.input_message()
        presenter.model.change_task_position(tasks, old_task_position, new_task_position)
