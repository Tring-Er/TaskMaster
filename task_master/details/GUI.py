from enum import Enum
from sys import exit as sys_exit

from tkinter import Tk, Button, Label, Text, END

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from entities.Task import Task
from details.TextFile import TextFile
from use_cases.TasksManager import TasksManager


class Messages(Enum):
    """All the constants used by the GUI"""

    EXIT_BUTTON_TEXT = "Exit"
    COMPLETE_LABEL = " COMPLETED"
    PROJECT_TITLE = "Task Master"
    ADD_TASK_BUTTON = "Add task"
    REMOVE_TASK_BUTTON = "Remove task"
    ORDER_TASK_BUTTON = "Order task"
    COMPLETE_OR_UNCOMPLETE_BUTTON = "Complete/Uncomplete"
    EXPORT_BUTTON = "Export"
    LIGHT_MODE_BUTTON = "Light"
    DARK_MODE_BUTTON = "Dark"


class GUI(Sendable, Readable):

    task_to_move = None

    def __init__(self) -> None:
        self._homepage = None
        self._create_homepage()
        self._create_widjets()
        self._show_widjets()
        self._text_file = TextFile()
    
    def send(self, tasks: list[Task]) -> None:
        tasks_string = ""
        for task in tasks:
            tasks_string += self.task_to_string(task)
        self._tasks_list.config(text=tasks_string)
    
    def read(self) -> list[Task]:
        tasks_text = self._tasks_list["text"].split("\n")[:-1]
        tasks = []
        for text in tasks_text:
            tasks.append(self.string_to_task(text))
        return tasks
    
    def task_to_string(self, task: Task) -> str:
        if task.is_completed:
            return f"{task.text}{Messages.COMPLETE_LABEL.value}\n"
        return f"{task.text}\n"
    
    def string_to_task(self, text: str) -> Task:
        if text.endswith(Messages.COMPLETE_LABEL.value):
            parsed_text = text.replace(Messages.COMPLETE_LABEL.value, "")
            return Task(parsed_text, True)
        return Task(text)
    
    def run(self) -> None:
        self.send(self._text_file.read())
        self._homepage.mainloop()
    
    def _create_homepage(self) -> None:
        self._homepage = Tk()
        screen_width = self._homepage.winfo_screenwidth()
        screen_height = self._homepage.winfo_screenheight()
        window_width = int(screen_width * 0.75)
        window_height = int(screen_height * 0.75)
        x_coord = int(screen_width/2) - int(window_width/2)
        y_coord = int(screen_height/2) - int(window_height/2)
        centered_geometry = f"{window_width}x{window_height}+{x_coord}+{y_coord}"
        self._homepage.geometry(centered_geometry)
        self._homepage.attributes("-type", "splash")
    
    def _create_widjets(self) -> None:
        title_font = ("San-Serif", 25)
        self._task_box = Text(self._homepage, height=1, width=25)
        self._title = Label(self._homepage, text=Messages.PROJECT_TITLE.value, font=title_font)
        self._tasks_list = Label(self._homepage)
        self._add_task_button = Button(self._homepage,
                                       text=Messages.ADD_TASK_BUTTON.value,
                                       command=self.add_task)
        self._remove_task_button = Button(self._homepage,
                                          text=Messages.REMOVE_TASK_BUTTON.value,
                                          command=self.remove_task)
        self._order_task_button = Button(self._homepage,
                                         text=Messages.ORDER_TASK_BUTTON.value,
                                         command=self.change_order)
        self._complete_or_uncomplete_task = Button(self._homepage,
                                                   text=Messages.COMPLETE_OR_UNCOMPLETE_BUTTON.value,
                                                   command=self.complete_on_uncomplete_task)
        self._export_tasks_button = Button(self._homepage,
                                           text=Messages.EXPORT_BUTTON.value,
                                           command=self.export_tasks)
        self._quit_button = Button(self._homepage,
                             text=Messages.EXIT_BUTTON_TEXT.value,
                             command=self.program_exit)
        self._light_mode = Button(self._homepage, text=Messages.LIGHT_MODE_BUTTON.value)
        self._dark_mode = Button(self._homepage, text=Messages.DARK_MODE_BUTTON.value)
    
    def _show_widjets(self) -> None:
        self._title.pack()
        self._add_task_button.pack()
        self._remove_task_button.pack()
        self._order_task_button.pack()
        self._complete_or_uncomplete_task.pack()
        self._export_tasks_button.pack()
        self._task_box.pack()
        self._tasks_list.pack()
        self._quit_button.pack()
        self._light_mode.pack()
        self._dark_mode.pack()
    
    def _get_task_from_task_box(self) -> Task | None:
        task_text = self._task_box.get("1.0", END).replace("\n", "")
        self._task_box.delete("1.0", END)
        if task_text != "":
            return self.string_to_task(task_text)
    
    def program_exit(self) -> None:
        sys_exit(0)
    
    def add_task(self) -> None:
        task = self._get_task_from_task_box()
        if task is not None:
            TasksManager.add_task(task, self._text_file)
            self.send(self._text_file.read())
    
    def remove_task(self) -> None:
        task = self._get_task_from_task_box()
        if task is not None:
            TasksManager.remove_task(task, self._text_file)
            self.send(self._text_file.read())
    
    def change_order(self) -> None:
        task = self._get_task_from_task_box()
        if task is not None:
            if GUI.task_to_move is not None:
                TasksManager.change_task_order(GUI.task_to_move, task, self._text_file)
                GUI.task_to_move = None
                self.send(self._text_file.read())
                return
            GUI.task_to_move = task
    
    def export_tasks(self) -> None:
        self._text_file.export_tasks()
    
    def complete_on_uncomplete_task(self) -> None:
        task = self._get_task_from_task_box()
        task = TasksManager.get_task(task, self._text_file)
        if task is not None:
            if task.is_completed:
                TasksManager.mark_task_as_not_completed(task, self._text_file)
            if not task.is_completed:
                TasksManager.mark_task_as_completed(task, self._text_file)
            self.send(self._text_file.read())
