"""This file contains a class used to manage all Task objects
from retriving them to save them
"""


from use_cases.external_interfaces.Sendable import Sendable
from use_cases.external_interfaces.Readable import Readable
from entities.Task import Task


class TasksManager:
    
    @staticmethod
    def add_task(sendable: Sendable, task: Task) -> None:
        sendable.send(task)
    
    @staticmethod
    def read_tasks(readable: Readable) -> list[Task]:
        return readable.read()
