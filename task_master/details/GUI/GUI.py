from sys import exit as sys_exit

from tkinter import Tk, Button, Label, Text, Frame, END
from tkinter.font import Font

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from use_cases.TasksManager import TasksManager
from entities.Task import Task
from details.TextFile import TextFile
from details.GUI.constants import *
from details.GUI.Themes import Themes
from details.GUI.widgets.Window import Window


class GUI(Sendable, Readable):

    def __init__(self, icon_path: str, tasks_file_path: str, exported_tasks_file_path: str) -> None:
        self.task_to_move = None
        self.current_theme = Themes.LIGHT_MODE
        self.create_widjets(icon_path)
        self.show_widjets()
        self.text_file = TextFile(tasks_file_path, exported_tasks_file_path)
    
    def send(self, tasks: list[Task]) -> None:
        tasks_string = ""
        for task in tasks:
            tasks_string += self.task_to_string(task)
        self.tasks_list.config(text=tasks_string)
    
    def read(self) -> list[Task]:
        tasks_text = self.tasks_list["text"].split("\n")[:-1]
        tasks = []
        for text in tasks_text:
            tasks.append(self.string_to_task(text))
        return tasks
    
    def task_to_string(self, task: Task) -> str:
        if task.is_completed:
            return f"{task.text}{COMPLETE_LABEL}\n"
        return f"{task.text}\n"
    
    def string_to_task(self, text: str) -> Task:
        if text.endswith(COMPLETE_LABEL):
            parsed_text = text.replace(COMPLETE_LABEL, "")
            return Task(parsed_text, True)
        return Task(text)
    
    def run(self) -> None:
        self.send(self.text_file.read())
        self.main_window.show()
    
    def create_window_widget(self, icon_path: str) -> None:
        self.main_window = Window(PROJECT_TITLE, icon_path, 0.75, 0.75)
        self.main_window.create()
    
    def create_frame_widgets(self) -> None:
        self.title_frame = Frame(self.main_window.tk_object, bg="#421C6F")
        self.options_frame = Frame(self.main_window.tk_object, bg="#9562C4")
        self.tasks_frame = Frame(self.main_window.tk_object)
        self.color_mode_frame = Frame(self.options_frame, bg="#9562C4")
    
    def create_text_widgets(self) -> None:
        self.task_box = Text(self.tasks_frame, height=1, width=25)
    
    def create_label_widgets(self) -> None:
        title_font = Font(family="Nexa Rust Slab Black Shadow 01", size=25)
        self.title = Label(self.title_frame,
                            text=PROJECT_TITLE,
                            font=title_font,
                            bg="#421C6F",
                            fg="white")
        self.tasks_list = Label(self.tasks_frame)
    
    def create_button_widgets(self) -> None:
        buttons_font = Font(family="Helvetica", size=12)
        self.add_task_button = Button(self.options_frame,
                                       text=ADD_TASK_BUTTON,
                                       font=buttons_font,
                                       command=self.add_task,
                                       bg="#9562C4",
                                       activebackground='#9562C4',
                                       fg="white")
        self.remove_task_button = Button(self.options_frame,
                                          text=REMOVE_TASK_BUTTON,
                                          font=buttons_font,
                                          command=self.remove_task,
                                          bg="#9562C4",
                                          activebackground='#9562C4',
                                          fg="white")
        self.order_task_button = Button(self.options_frame,
                                         text=ORDER_TASK_BUTTON,
                                         font=buttons_font,
                                         command=self.change_order,
                                         bg="#9562C4",
                                         activebackground='#9562C4',
                                         fg="white")
        self.complete_or_uncomplete_task = Button(self.options_frame,
                                                   text=COMPLETE_OR_UNCOMPLETE_BUTTON,
                                                   font=buttons_font,
                                                   command=self.complete_on_uncomplete_task,
                                                   bg="#9562C4",
                                                   activebackground='#9562C4',
                                                   fg="white")
        self.export_tasks_button = Button(self.options_frame,
                                           text=EXPORT_BUTTON,
                                           font=buttons_font,
                                           command=self.export_tasks,
                                           bg="#9562C4",
                                           activebackground='#9562C4',
                                           fg="white")
        self.quit_button = Button(self.options_frame,
                             text=EXIT_BUTTON_TEXT,
                             font=buttons_font,
                             command=self.program_exit,
                             bg="#9562C4",
                             activebackground='#9562C4',
                             fg="white")
        self.swap_theme_button = Button(self.options_frame,
                                  text=LIGHT_MODE_BUTTON,
                                  font=buttons_font,
                                  command=self.swap_theme_mode)
    
    def create_widjets(self, icon_path: str) -> None:
        self.create_window_widget(icon_path)
        self.create_frame_widgets()
        self.create_text_widgets()
        self.create_label_widgets()
        self.create_button_widgets()
    
    def show_widjets(self) -> None:
        self.title_frame.pack(side="top", fill="x")
        self.options_frame.pack(side="left", fill="y")
        self.tasks_frame.pack(side="left", fill="both", expand=True)
        self.title.pack(side="left")
        self.add_task_button.pack(fill="x")
        self.remove_task_button.pack(fill="x")
        self.order_task_button.pack(fill="x")
        self.complete_or_uncomplete_task.pack(fill="x")
        self.export_tasks_button.pack(fill="x")
        self.task_box.pack(fill="x")
        self.tasks_list.pack()
        self.swap_theme_button.pack(side="bottom", fill="x")
        self.quit_button.pack(side="bottom", fill="x")
    
    def get_task_from_task_box(self) -> Task | None:
        task_text = self.task_box.get("1.0", END).replace("\n", "")
        self.task_box.delete("1.0", END)
        if task_text != "":
            return self.string_to_task(task_text)
    
    def program_exit(self) -> None:
        sys_exit(0)
    
    def add_task(self) -> None:
        task = self.get_task_from_task_box()
        if task is not None:
            TasksManager.add_task(task, self.text_file)
            self.send(self.text_file.read())
    
    def remove_task(self) -> None:
        task = self.get_task_from_task_box()
        if task is not None:
            TasksManager.remove_task(task, self.text_file)
            self.send(self.text_file.read())
    
    def change_order(self) -> None:
        task = self.get_task_from_task_box()
        if task is not None:
            if self.task_to_move is not None:
                TasksManager.change_task_order(self.task_to_move, task, self.text_file)
                self.task_to_move = None
                self.send(self.text_file.read())
                return
            self.task_to_move = task
    
    def export_tasks(self) -> None:
        self.text_file.export_tasks()
    
    def complete_on_uncomplete_task(self) -> None:
        task = self.get_task_from_task_box()
        task = TasksManager.get_task(task, self.text_file)
        if task is not None:
            if task.is_completed:
                TasksManager.mark_task_as_not_completed(task, self.text_file)
            if not task.is_completed:
                TasksManager.mark_task_as_completed(task, self.text_file)
            self.send(self.text_file.read())
    
    def swap_theme_mode(self) -> None:
        if self.current_theme is Themes.LIGHT_MODE:
            self.set_dark_mode()
            self.swap_theme_button["text"] = DARK_MODE_BUTTON
        else:
            self.set_light_mode()
            self.swap_theme_button["text"] = LIGHT_MODE_BUTTON
    
    def set_dark_mode(self) -> None:
        self.title["fg"] = "black"
        self.tasks_frame["bg"] = "black"
        self.tasks_list["bg"] = "black"
        self.tasks_list["fg"] = "white"
        self.current_theme = Themes.DARK_MODE
    
    def set_light_mode(self) -> None:
        self.title["fg"] = "white"
        self.tasks_frame["bg"] = "#f0f0f0"
        self.tasks_list["bg"] = "#f0f0f0"
        self.tasks_list["fg"] = "black"
        self.current_theme = Themes.LIGHT_MODE
