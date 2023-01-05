"""This mode adds a task to the tasks file"""

from presenter.modes.mode import Mode
from presenter.presenter import Presenter


class AddTask(Mode):
    """This class execute the code to add a task to the tasks file"""

    CLI_COMMAND = "w"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.view.print_message("Insert a task to save")
        message = presenter.view.input_message()
        presenter.model.add_task(message)
