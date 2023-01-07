"""Contains FileOpener class"""


class FileOpener:
    """It opens and convert tasks file"""

    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path

    def get_tasks_from_file(self) -> list[str]:
        """It opens the file containing tasks

        Args:
            path (str): The absolute path of the tasks file

        Returns:
            str: The lines contained in the file
        """

        with open(self.__file_path, "r", encoding="utf-8") as tasks_file:
            return tasks_file.readlines()

    def add_task_to_file(self, task: str) -> None:
        """Add the task passed to the path passed

        Args:
            path (str): The tasks file absolute path
            task (str): The task to add
        """

        with open(self.__file_path, "a", encoding="utf-8") as tasks_file:
            tasks_file.write(task)

    def overwrite_tasks_file(self, tasks: list[str]) -> None:
        """Overwrite the tasks file with the tasks list provided

        Args:
            tasks (list[str]): The tasks list to overwrite with
        """

        with open(self.__file_path, "w", encoding="utf-8") as tasks_file:
            tasks_file.writelines(tasks)


def create_file_opener(file_path: str) -> FileOpener:
    """Create an instance of the FileOpener class

    Args:
        file_path (str): Path to pass to the FileOpener init

    Returns:
        FileOpener: FileOpener instance
    """

    return FileOpener(file_path)
