"""This file contains an object to use txt files to store and read from it"""


import os

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from entities.Task import Task
from Loader import TASKS_FOLDER


TASKS_FILE_PATH = os.path.join(TASKS_FOLDER, r"tasks.txt")
EXPORTED_TASKS_FILE_PATH = os.path.join(TASKS_FOLDER, r"exported_tasks.txt")
_COMPLETED_LABEL = " COMPLETED"


class TextFile(Readable, Sendable):

    def __init__(self) -> None:
        self.create_file_if_not_present()
    
    def create_file_if_not_present(self) -> None:
        with open(TASKS_FILE_PATH, "a", encoding="utf-8"):
            ...
    
    def read(self) -> list[Task]:
        tasks = []
        with open(TASKS_FILE_PATH, "r", encoding="utf-8") as tasks_file:
            for task_line in tasks_file.readlines():
                tasks.append(self.text_to_task(task_line))
        return tasks
    
    def send(self, tasks: list[Task]) -> None:
        with open(TASKS_FILE_PATH, "w", encoding="utf-8") as tasks_file:
            for task in tasks:
                task_text = self.task_to_text(task)
                tasks_file.write(task_text)

    def export_tasks(self) -> None:
        """Exports all the data from the tasks file"""

        with open(TASKS_FILE_PATH, "r", encoding="utf-8") as file_tasks:
            file_content = file_tasks.readlines()
        with open(EXPORTED_TASKS_FILE_PATH, "w", encoding="utf-8") as export_file:
            export_file.writelines(file_content)
    
    def text_to_task(self, text: str) -> Task:
        parsed_task_text = text.replace("\n", "")
        if parsed_task_text.endswith(_COMPLETED_LABEL):
            task_text = parsed_task_text.replace(_COMPLETED_LABEL, "")
            return Task(task_text, True)
        return Task(parsed_task_text)
    
    def task_to_text(self, task: Task) -> str:
        if task.is_completed:
            return f"{task.text}{_COMPLETED_LABEL}\n"
        return task.text + "\n"
