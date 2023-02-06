"""Start of project"""

from model.task_manager import TaskManager
from view.cli import CLI
# from view.gui import GUI
from presenter.cli.console_manager import ConsoleManager
# from presenter.gui.gui_manager import GUIManager


def main() -> None:
    """Main func"""

    model = TaskManager()
    view = CLI()
    presenter = ConsoleManager(model, view)
    
    #view = GUI()
    #presenter = GUIManager(model, view)
    
    view = CLI()
    presenter = ConsoleManager(model, view)
    presenter.compute()


if __name__ == "__main__":
    main()
