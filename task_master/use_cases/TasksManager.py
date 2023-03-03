"""This file contains a class used to manage all Task objects
from retriving them to save them
"""

from typing import Callable

from use_cases.external_interfaces.Sendable import Sendable
from use_cases.external_interfaces.Readable import Readable
from entities.Task import Task


class TasksManager:

    @staticmethod
    def read_tasks(readable: Readable) -> list[Task]:
        return readable.read()
    
    @staticmethod
    def write_tasks(tasks: list[Task], sendable: Sendable) -> None:
        sendable.send(tasks)
    
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
    def change_order(old_task_index: int, new_task_index: int, readable: Readable, sendable: Sendable = None) -> None:
        if sendable is None:
            sendable = readable
        tasks = TasksManager.read_tasks(readable)
        tasks[old_task_index], tasks[new_task_index] = tasks[new_task_index], tasks[old_task_index]
        TasksManager.write_tasks(tasks, sendable)
    
    @staticmethod
    def change_task_order(task_to_move: Task, task_to_leave: Task, readable: Readable, sendable: Sendable = None) -> None:
        tasks = TasksManager.read_tasks(readable)
        task_to_move_index = None
        task_to_leave_index = None
        for task_index, task in enumerate(tasks):
            if task_to_move.text == task.text:
                task_to_move_index = task_index
            if task_to_leave.text == task.text:
                task_to_leave_index = task_index
        TasksManager.change_order(task_to_move_index, task_to_leave_index, readable, sendable)
    
    @staticmethod
    def mark_task_as_completed(task: Task, readable: Readable, sendable: Sendable = None) -> None:
        TasksManager.mark_task_as(TasksManager.complete, task, readable, sendable)
    
    @staticmethod
    def mark_task_as_not_completed(task: Task, readable: Readable, sendable: Sendable = None) -> None:
        TasksManager.mark_task_as(TasksManager.not_completed, task, readable, sendable)
    
    @staticmethod
    def mark_task_as(option: Callable[[Task], None], task: Task, readable: Readable, sendable: Sendable = None) -> None:
        if sendable is None:
            sendable = readable
        tasks = readable.read()
        for _task in tasks:
            if _task.text == task.text:
                option(_task)
        sendable.send(tasks)

    @staticmethod
    def complete(task: Task) -> None:
        task.complete()

    @staticmethod
    def not_completed(task: Task) -> None:
        task.uncomplete()
    
    @staticmethod
    def get_task(task: str | Task, readable: Readable) -> Task | None:
        tasks = readable.read()
        for _task in tasks:
            if task.text == _task.text:
                return _task
