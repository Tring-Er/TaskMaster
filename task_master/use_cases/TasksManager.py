"""This file contains a class used to manage all Task objects
from retriving them to save them
"""


from use_cases.external_interfaces.Sendable import Sendable
from use_cases.external_interfaces.Readable import Readable
from entities.Task import Task


class TasksManager:
    
    @staticmethod
    def add_task(task: Task, sendable: Sendable, readable: Readable = None) -> None:
        if readable is None:
            readable = sendable
        tasks = TasksManager.read_tasks(readable)
        tasks.append(task)
        TasksManager.write_tasks(tasks, sendable)
    
    @staticmethod
    def remove_task(task: Task, readable: Readable, sendable: Sendable = None) -> None:
        if sendable is None:
            sendable = readable
        tasks = TasksManager.read_tasks(readable)
        for _task in tasks:
            if task.text == _task.text:
                tasks.remove(_task)
        TasksManager.write_tasks(tasks, sendable)
    
    @staticmethod
    def read_tasks(readable: Readable) -> list[Task]:
        return readable.read()
    
    @staticmethod
    def write_tasks(tasks: list[Task], sendable: Sendable) -> None:
        sendable.send(tasks)
    
    @staticmethod
    def change_oder(old_task_index: int, new_task_index: int, readable: Readable, sendable: Sendable = None):
        if sendable is None:
            sendable = readable
        tasks = TasksManager.read_tasks(readable)
        tasks[old_task_index], tasks[new_task_index] = tasks[new_task_index], tasks[old_task_index]
        TasksManager.write_tasks(tasks, sendable)
