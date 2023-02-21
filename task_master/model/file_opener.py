"""Contains FileOpener class"""

from os import getcwd

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from entities.Task import Task


DIRETORY = getcwd() + r"/task_master/model"
FILE_PATH = DIRETORY + r"/tasks.txt"
EXPORT_FILE_PATH = DIRETORY + r"/exported_tasks.txt"


class FileManager(Readable, Sendable):
    """It opens and convert tasks file"""
    
    def read(self) -> list[Task]:
        tasks = []
        with open(FILE_PATH, "r", encoding="utf-8") as tasks_file:
            for task_line in tasks_file.readlines():
                parsed_task = task_line.replace("\n", "")
                tasks.append(Task(parsed_task))
        return tasks
    
    def send(self, tasks: list[Task]) -> None:
        with open(FILE_PATH, "w", encoding="utf-8") as tasks_file:
            for task in tasks:
                # add new line char (write this when adding a converter)
                tasks_file.write(task.text + "\n")

    def export_tasks(self) -> None:
        """Exports all the data from the tasks file"""

        with open(FILE_PATH, "r", encoding="utf-8") as file_tasks:
            file_content = file_tasks.readlines()
        with open(EXPORT_FILE_PATH, "w", encoding="utf-8") as export_file:
            export_file.writelines(file_content)


def create_file_manager() -> FileManager:
    """Create an instance of the FileOpener class

    Args:
        file_path (str): Path to pass to the FileOpener init

    Returns:
        FileOpener: FileOpener instance
    """

    return FileManager()
