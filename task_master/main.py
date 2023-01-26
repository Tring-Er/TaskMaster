"""Start of project"""

from model.task_manager import TaskManager
#from view.cli import CLI
from view.gui import GUI
#from presenter.console_manager import ConsoleManager
from presenter.gui_manager import GUIManager


def main() -> None:
    """Main func"""

    model = TaskManager()
    view = GUI()  # CLI()
    presenter = GUIManager(model, view)  # ConsoleManager(model, view)
    presenter.compute()


if __name__ == "__main__":
    main()
