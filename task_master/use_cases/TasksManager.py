"""This file contains a class used to manage all Task objects
from retriving them to save them
"""

from typing import Callable

from entities.Task import Task


class TasksManager:
    
    @staticmethod
    def add_task(tasks: list[Task], task: Task) -> list[Task]:
        tasks.append(task)
        return tasks
    
    @staticmethod
    def remove_task(tasks: list[Task], task: Task) -> list[Task]:
        for stored_task in tasks:
            if task.text == stored_task.text:
                tasks.remove(stored_task)
        return tasks
    
    @staticmethod
    def change_order(tasks: list[Task], old_task_index: int, new_task_index: int) -> list[Task]:
        tasks[old_task_index], tasks[new_task_index] = tasks[new_task_index], tasks[old_task_index]
        return tasks
    
    @staticmethod
    def change_task_order(tasks: list[Task], task_to_move: Task, task_to_leave: Task) -> list[Task]:
        task_to_move_index = None
        task_to_leave_index = None
        for task_index, task in enumerate(tasks):
            if task_to_move.text == task.text:
                task_to_move_index = task_index
            if task_to_leave.text == task.text:
                task_to_leave_index = task_index
        new_tasks_list = TasksManager.change_order(tasks, task_to_move_index, task_to_leave_index)
        return new_tasks_list
    
    @staticmethod
    def mark_task_as_completed(tasks: list[Task], task: Task) -> list[Task]:
        return TasksManager.mark_task_as(TasksManager.complete, tasks, task)
    
    @staticmethod
    def mark_task_as_not_completed(tasks: list[Task], task: Task) -> list[Task]:
        return TasksManager.mark_task_as(TasksManager.not_completed, tasks, task)
    
    @staticmethod
    def mark_task_as(option: Callable[[Task], None], tasks: list[Task], task: Task) -> list[Task]:
        for _task in tasks:
            if task.text == _task.text:
                option(_task)
                break
        return tasks

    @staticmethod
    def complete(task: Task) -> None:
        task.complete()

    @staticmethod
    def not_completed(task: Task) -> None:
        task.uncomplete()
    
    @staticmethod
    def get_task(tasks: list[Task], task: str | Task) -> Task | None:
        for _task in tasks:
            if task.text == _task.text:
                return _task
