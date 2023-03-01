from details.Console import Console
from details.GUI import GUI


def main() -> None:
    gui_mode = True
    if gui_mode:
        gui = GUI()
        gui.run()
    else:
        console = Console()
        console.run()


if __name__ == "__main__":
    main()
