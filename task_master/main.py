from details.Console import Console
from details.GUI.GUI import GUI
from Program import Program


RUN_IN_GUI_MODE = True


def main() -> None:
    program = Program()
    tasks_file_path = program.get_tasks_file_path()
    exported_tasks_file_path = program.get_exported_tasks_file_path()
    if RUN_IN_GUI_MODE:
        gui = GUI(program.get_title_bar_icon_path(), tasks_file_path, exported_tasks_file_path)
        gui.run()
    else:
        console = Console(tasks_file_path, exported_tasks_file_path)
        console.run()


if __name__ == "__main__":
    main()
