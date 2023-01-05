"""Start of project"""

from model.task_manager import TaskManager
from view.cli import CLI
from presenter.console_manager import ConsoleManager


def main() -> None:
    """Main func"""

    presenter = ConsoleManager(TaskManager, CLI)
    presenter.compute()


if __name__ == "__main__":
    main()
