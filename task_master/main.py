"""Start of project"""

from model.task_manager import TaskManager
from view.cli import CLI
from presenter.console_manager import ConsoleManager


TASK_FILE_PATH = r"C:\Altro\taskmaster\task_master\model\tasks.txt"


def main() -> None:
    """Main func"""

    model = TaskManager(TASK_FILE_PATH)
    view = CLI()
    presenter = ConsoleManager(model, view)
    presenter.compute()


if __name__ == "__main__":
    main()
