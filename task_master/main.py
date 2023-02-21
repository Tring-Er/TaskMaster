"""Start of project"""

#from details.CLI import CLI

from presenter.cli.console_manager import ConsoleManager


def main() -> None:
    """Main func"""
    # the tasks file get created at program start if not present
    
    #view = GUI()
    #presenter = GUIManager(model, view)
    
    presenter = ConsoleManager()
    presenter.compute()


if __name__ == "__main__":
    main()
