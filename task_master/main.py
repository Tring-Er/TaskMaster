"""Start of project"""
#this is a test

#from details.CLI import CLI

from model.task_manager import TaskManager
from view.cli import CLI
from presenter.cli.console_manager import ConsoleManager


def main() -> None:
    """Main func"""
    # the tasks file get created at program start if not present

    #CLI().print_task()

    model = TaskManager()
    view = CLI()
    
    #view = GUI()
    #presenter = GUIManager(model, view)
    
    presenter = ConsoleManager(model, view)
    presenter.compute()


if __name__ == "__main__":
    main()
