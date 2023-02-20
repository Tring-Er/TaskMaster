"""Contains FileOpener class"""

from os import getcwd

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from entities.Task import Task


class FileManager(Readable, Sendable):
    """It opens and convert tasks file"""

    def __init__(self) -> None:
        directory = getcwd() + r"/task_master/model"
        self.__file_path = directory + r"/tasks.txt"
        self.__export_file_path = directory + r"/exported_tasks.txt"
    
    def read(self) -> list[Task]:
        tasks = []
        raw_tasks = self.get_tasks()
        for raw_task in raw_tasks:
            tasks.append(Task(raw_task))
        return tasks
    
    def send(self, task: Task) -> None:
        self.add_task(task.text)

    def get_tasks(self) -> list[str]:
        """It opens the file containing tasks

        Args:
            path (str): The absolute path of the tasks file

        Returns:
            str: The lines contained in the file
        """

        with open(self.__file_path, "r", encoding="utf-8") as tasks_file:
            return tasks_file.readlines()

    def add_task(self, task: str) -> None:
        """Add the task passed to the path passed

        Args:
            path (str): The tasks file absolute path
            task (str): The task to add
        """

        with open(self.__file_path, "a", encoding="utf-8") as tasks_file:
            tasks_file.write(task)

    def overwrite_tasks(self, tasks: list[str]) -> None:
        """Overwrite the tasks file with the tasks list provided

        Args:
            tasks (list[str]): The tasks list to overwrite with
        """

        with open(self.__file_path, "w", encoding="utf-8") as tasks_file:
            tasks_file.writelines(tasks)

    def export_tasks(self) -> None:
        """Exports all the data from the tasks file"""

        with open(self.__file_path, "r", encoding="utf-8") as file_tasks:
            file_content = file_tasks.readlines()
        with open(self.__export_file_path, "w", encoding="utf-8") as export_file:
            export_file.writelines(file_content)


def create_file_manager() -> FileManager:
    """Create an instance of the FileOpener class

    Args:
        file_path (str): Path to pass to the FileOpener init

    Returns:
        FileOpener: FileOpener instance
    """

    return FileManager()
