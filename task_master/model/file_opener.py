"""Contains FileOpener class"""


class FileOpener:
    """It opens and convert tasks file"""

    @staticmethod
    def get_tasks_from_file(path: str) -> str:
        """It opens the file containing tasks

        Args:
            path (str): The absolute path of the tasks file

        Returns:
            str: The lines contained in the file
        """

        with open(path, "r", encoding="utf-8") as tasks_file:
            return tasks_file.readlines()

    @staticmethod
    def add_task_to_file(path: str, task: str) -> None:
        """Add the task passed to the path passed

        Args:
            path (str): The tasks file absolute path
            task (str): The task to add
        """

        with open(path, "a", encoding="utf-8") as tasks_file:
            tasks_file.write(task)
