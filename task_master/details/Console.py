from enum import Enum
from sys import exit as sys_exit

from details.TextFile import TextFile
from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from use_cases.TasksManager import TasksManager
from entities.Task import Task


class Messages(Enum):
    """All Messages used by console_manager"""

    CHOOSE_MODE = "Select mode ({})"
    ASK_FOR_TASK = "Insert a task to save"
    EXIT_MESSAGE = "Quitting the program..."
    TASKS_EXPORTED = "Tasks exported!"
    INVALID_MODE_SELECTED = "The input inserted was not a valid mode!"
    SELECT_TASK_TO_REMOVE = "Select a task to remove"
    NO_NUMBER_FOUND = "No task found with that number"
    SELECT_TASK_TO_MOVE = "Select a task to change position"
    SELECT_POSITION = "Select the position to move the task to"
    SELECT_THE_TASK_TO_COMPLETE = "Select the task to mark as completed"
    SELECT_THE_TASK_TO_UNCOMPLETE = "Select the task to mark as not completed"
    TASK_COMPLETE_LABEL = " COMPLETED"


class Console(Readable, Sendable):

    LOCAL_SYMBOLS = {"add task",
                     "exit",
                     "export tasks",
                     "",
                     "read tasks",
                     "remove task",
                     "task order",
                     "complete task",
                     "uncomplete task"}
    
    def __init__(self) -> None:
        self.file_manager = TextFile()
    
    def run(self) -> None:
        """Make the program run"""

        modes_symbols = self.get_modes_simbols()
        while True:
            self.print_message(Messages.CHOOSE_MODE.value.format(modes_symbols))
            selected_mode = self.input_message()
            match selected_mode:
                case "add task":
                    self.add_task()
                case "exit":
                    self.exit()
                case "export tasks":
                    self.export_tasks()
                case "read tasks":
                    self.read_tasks()
                case "remove task":
                    self.remove_task()
                case "task order":
                    self.task_order()
                case "complete task":
                    self.set_task_as_completed()
                case "uncomplete task":
                    self.set_task_as_not_completed()
                case _:
                    self.invalid_mode()
    
    def read(self) -> list[Task]:
        message = self.input_message()
        return [self.str_to_task(message)]
    
    def send(self, tasks: list[Task]) -> None:
        for task_index, task in enumerate(tasks, 1):
            message = f"{task_index}- {self.task_to_str(task)}"
            self.print_message(message)
    
    def str_to_task(self, text: str) -> Task:
        if text.endswith(Messages.TASK_COMPLETE_LABEL.value):
            task_text = text.replace(Messages.TASK_COMPLETE_LABEL.value, "")
            return Task(task_text, True)
        return Task(text)
    
    def task_to_str(self, task: Task) -> str:
        if task.is_completed:
            return f"{task.text}{Messages.TASK_COMPLETE_LABEL.value}"
        return f"{task.text}"
    
    def print_message(self, message: str) -> None:
        """It prints the message on the console

        Args:
            message (str): the message to print
        """
        print(message)
    
    def input_message(self) -> str:
        """Return the input passed in the console

        Returns:
            str: The string inserted by user
        """
        return input()
    
    def get_modes_simbols(self) -> str:
        modes_symbols = self.LOCAL_SYMBOLS.copy()
        modes_symbols.remove("")
        parsed_modes_symbols = "/".join(modes_symbols)
        return parsed_modes_symbols
    
    def add_task(self) -> None:
        self.print_message(Messages.ASK_FOR_TASK.value)
        message = self.input_message()
        TasksManager.add_task(self.str_to_task(message), self.file_manager)
    
    def exit(self) -> None:
        self.print_message(Messages.EXIT_MESSAGE.value)
        sys_exit(0)
    
    def export_tasks(self) -> None:
        self.file_manager.export_tasks()
        self.print_message(Messages.TASKS_EXPORTED.value)
    
    def invalid_mode(self) -> None:
        self.print_message(Messages.INVALID_MODE_SELECTED.value)
    
    def read_tasks(self) -> None:
        tasks_list = TasksManager.read_tasks(self.file_manager)
        self.send(tasks_list)
    
    def remove_task(self) -> None:
        tasks = TasksManager.read_tasks(self.file_manager)
        self.send(tasks)
        self.print_message(Messages.SELECT_TASK_TO_REMOVE.value)
        task_number_to_remove = self.input_message()
        task_index_to_remove = int(task_number_to_remove) - 1
        try:
            TasksManager.remove_task(tasks[task_index_to_remove], self.file_manager)
        except IndexError:
            self.print_message(Messages.NO_NUMBER_FOUND.value)
    
    def task_order(self) -> None:
        tasks = TasksManager.read_tasks(self.file_manager)
        self.send(tasks)
        self.print_message(Messages.SELECT_TASK_TO_MOVE.value)
        old_task_index = int(self.input_message()) - 1
        self.print_message(Messages.SELECT_POSITION.value)
        new_task_index = int(self.input_message()) - 1
        TasksManager.change_order(old_task_index, new_task_index, self.file_manager)
    
    def set_task_as_completed(self) -> None:
        tasks = TasksManager.read_tasks(self.file_manager)
        self.send(tasks)
        self.print_message(Messages.SELECT_THE_TASK_TO_COMPLETE.value)
        task_index = int(self.input_message()) - 1
        TasksManager.mark_task_as_completed(tasks[task_index], self.file_manager)
    
    def set_task_as_not_completed(self) -> None:
        tasks = TasksManager.read_tasks(self.file_manager)
        self.send(tasks)
        self.print_message(Messages.SELECT_THE_TASK_TO_UNCOMPLETE.value)
        task_index = int(self.input_message()) - 1
        TasksManager.mark_task_as_not_completed(tasks[task_index], self.file_manager)

