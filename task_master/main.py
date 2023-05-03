from details.Console import Console
from details.gui.GUI import GUI


RUN_IN_GUI_MODE = True


def main() -> None:
    if RUN_IN_GUI_MODE:
        gui = GUI()
        gui.run()
    else:
        console = Console()
        console.run()


if __name__ == "__main__":
    main()
