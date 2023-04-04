from details.Console import Console
from details.GUI import GUI
from Loader import Loader


def main() -> None:
    Loader.startup()
    gui_mode = True
    if gui_mode:
        gui = GUI(Loader.get_title_bar_icon())
        gui.run()
    else:
        console = Console()
        console.run()


if __name__ == "__main__":
    main()
