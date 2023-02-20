"""Start of project"""

from model.task_manager import TaskManager
from view.cli import CLI
# from view.gui import GUI
from presenter.cli.console_manager import ConsoleManager
# from presenter.gui.gui_manager import GUIManager
from entities.Task import Task


def main() -> None:
    """Main func"""
    # the tasks file get created at program start if not present

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
