from enum import Enum
from sys import exit as sys_exit

from tkinter import Tk, Button, Label

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from entities.Task import Task
from details.TextFile import TextFile


class Messages(Enum):
    """All the constants used by the GUI"""

    EXIT_BUTTON_TEXT = "exit"
    COMPLETE_LABEL = " COMPLETED"
    PROJECT_TITLE = "Task Master"


class GUI(Sendable, Readable):

    def __init__(self) -> None:
        self._homepage = None
        self._create_homepage()
        self._text_file = TextFile()
    
    def send(self, tasks: list[Task]) -> None:
        tasks_string = ""
        for task in tasks:
            tasks_string += self.task_to_string(task)
        self._tasks_list.config(text=tasks_string)
    
    def read(self) -> list[Task]:
        ...
    
    def task_to_string(self, task: Task) -> str:
        if task.is_completed:
            return f"{task.text}{Messages.COMPLETE_LABEL.value}\n"
        return f"{task.text}\n"
    
    def run(self) -> None:
        self.send(self._text_file.read())
        self._homepage.mainloop()
    
    def _create_homepage(self) -> None:
        self._homepage = Tk()
        screen_width = self._homepage.winfo_screenwidth()
        screen_height = self._homepage.winfo_screenheight()
        window_width = 600
        window_height = 300
        adjusted_width = int(screen_width/2) - int(window_width/2)
        adjusted_height = int(screen_height/2) - int(window_height/2)
        self._homepage.geometry(f"{window_width}x{window_height}+{adjusted_width}+{adjusted_height}")
        self._homepage.overrideredirect(True)
        self._title = Label(self._homepage, text=Messages.PROJECT_TITLE.value, font=("San-Serif", 25))
        self._title.pack()
        self._tasks_list = Label(self._homepage)
        self._tasks_list.pack()
        self._quit_button = Button(self._homepage,
                             text=Messages.EXIT_BUTTON_TEXT.value,
                             command=self.program_exit)
        self._quit_button.pack()
    
    def program_exit(self) -> None:
        sys_exit(0)
