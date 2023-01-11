"""Start of project"""

from model.task_manager import TaskManager
from view.cli import CLI
from presenter.console_manager import ConsoleManager


def main() -> None:
    """Main func"""

    model = TaskManager()
    view = CLI()
    presenter = ConsoleManager(model, view)
    presenter.compute()


if __name__ == "__main__":
    main()
