"""This file contains an object to use txt files to store and read from it"""


from os import getcwd

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from entities.Task import Task


DIRETORY = getcwd() + r"/task_master/details"
FILE_PATH = DIRETORY + r"/tasks.txt"
EXPORT_FILE_PATH = DIRETORY + r"/exported_tasks.txt"


class TextFile(Readable, Sendable):
    
    def read(self) -> list[Task]:
        tasks = []
        with open(FILE_PATH, "r", encoding="utf-8") as tasks_file:
            for task_line in tasks_file.readlines():
                tasks.append(self.text_to_task(task_line))
        return tasks
    
    def send(self, tasks: list[Task]) -> None:
        with open(FILE_PATH, "w", encoding="utf-8") as tasks_file:
            for task in tasks:
                task_text = self.task_to_text(task)
                tasks_file.write(task_text)

    def export_tasks(self) -> None:
        """Exports all the data from the tasks file"""

        with open(FILE_PATH, "r", encoding="utf-8") as file_tasks:
            file_content = file_tasks.readlines()
        with open(EXPORT_FILE_PATH, "w", encoding="utf-8") as export_file:
            export_file.writelines(file_content)
    
    def text_to_task(self, text: str) -> Task:
        parsed_task_text = text.replace("\n", "")
        return Task(parsed_task_text)
    
    def task_to_text(self, task: Task) -> str:
        return task.text + "\n"
