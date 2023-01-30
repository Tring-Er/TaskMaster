"""Start of project"""

#from sys import argv as sys_argv

from model.task_manager import TaskManager
from view.cli import CLI
# from view.gui import GUI
from presenter.console_manager import ConsoleManager
# from presenter.gui_manager import GUIManager


def main() -> None:
    """Main func"""

    model = TaskManager()
    #if len(sys_argv) > 1:
    #    view = CLI()
    #    presenter = ConsoleManager(model, view)
    #else:
    #    view = GUI()
    #    presenter = GUIManager(model, view)
    view = CLI()
    presenter = ConsoleManager(model, view)
    presenter.compute()


if __name__ == "__main__":
    main()
