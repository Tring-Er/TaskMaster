"""This module contains the an object that adds a task to the tasks file and all it's messages
used
"""

from enum import Enum

from presenter.cli.modes.mode import Mode
from presenter.presenter import Presenter
from entities.Task import Task
from use_cases.TasksManager import TasksManager
from model.file_opener import FileManager


class Messages(Enum):
    """Messages (string constants) used by the AddTask object"""

    ASK_FOR_TASK = "Insert a task to save"


class AddTask(Mode):
    """This class execute the code to add a task to the tasks file"""

    CLI_COMMAND = "add task"

    @staticmethod
    def execute(presenter: Presenter) -> None:
        presenter.print_message(Messages.ASK_FOR_TASK.value)
        message = presenter.input_message()
        TasksManager.add_task(AddTask.converter(message), FileManager())
    
    @staticmethod
    def converter(text: str) -> Task:
        return Task(text)
