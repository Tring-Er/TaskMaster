from sys import exit as sys_exit

from tkinter import END

from use_cases.external_interfaces.Readable import Readable
from use_cases.external_interfaces.Sendable import Sendable
from use_cases.TasksManager import TasksManager
from entities.Task import Task
from details.text_file.TextFile import TextFile
from details.gui.constants import *
from details.gui.Themes import Themes
from details.gui.widgets.Window import Window
from details.gui.widgets.Frame import Frame
from details.gui.widgets.Text import Text
from details.gui.widgets.Label import Label
from details.gui.widgets.Font import Font
from details.gui.widgets.Button import Button
from details.gui.loaders.FontLoader import FontLoader
from details.gui.loaders.IconLoader import IconLoader


class GUI(Sendable, Readable):

    def __init__(self) -> None:
        FontLoader.load_nexa_font()
        self.text_file = TextFile()
        self.task_to_move = None
        self.current_theme = Themes.LIGHT_MODE
        self.create_widjets()
        self.run()
    
    def send(self, tasks: list[Task]) -> None:
        tasks_string = ""
        for task in tasks:
            tasks_string += self.task_to_string(task)
        self.tasks_list.tk_object.config(text=tasks_string)
    
    def read(self) -> list[Task]:
        tasks_text = self.tasks_list.tk_object["text"].split("\n")[:-1]
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
    
    def create_window_widget(self) -> None:
        icon_path = IconLoader.get_title_bar_icon_path()
        self.main_window = Window()
        self.main_window.set_params(title=PROJECT_TITLE, icon_path=icon_path, percentage_of_screen_width_taken_by_window=0.75, percentage_of_screen_height_taken_by_window=0.75)
    
    def create_frame_widgets(self) -> None:
        self.title_frame = Frame()
        self.main_window.add_widget(self.title_frame)
        self.title_frame.set_params(background_color="#421C6F", position_options={"side": "top", "fill": "x"})
        self.options_frame = Frame()
        self.main_window.add_widget(self.options_frame)
        self.options_frame.set_params(background_color="#9562C4", position_options={"side": "left", "fill": "y"})
        self.tasks_frame = Frame()
        self.main_window.add_widget(self.tasks_frame)
        self.tasks_frame.set_params(background_color="#F0F0F0", position_options={"side": "left", "fill": "both", "expand": True})
    
    def create_text_widgets(self) -> None:
        self.task_box = Text()
        self.tasks_frame.add_widget(self.task_box)
        self.task_box.set_params(height=1, width=25, position_options={"fill": "x"})
    
    def create_label_widgets(self) -> None:
        title_font = Font(family="Nexa Rust Slab Black Shadow 01", size=25)
        self.title = Label()
        self.title_frame.add_widget(self.title)
        self.title.set_params(text=PROJECT_TITLE, font=title_font, background_color="#421C6F", foreground_color="white", position_options={"side": "left"})
        self.tasks_list = Label()
        self.tasks_frame.add_widget(self.tasks_list)
        self.tasks_list.set_params()
    
    def create_button_widgets(self) -> None:
        buttons_font = Font(family="Helvetica", size=12)
        self.add_task_button = Button()
        self.options_frame.add_widget(self.add_task_button)
        self.add_task_button.set_params(command=self.add_task, text=ADD_TASK_BUTTON, font=buttons_font, background_color="#9562C4", foreground_color="white", active_background_color='#9562C4', position_options={"fill": "x"})
        self.remove_task_button = Button()
        self.options_frame.add_widget(self.remove_task_button)
        self.remove_task_button.set_params(command=self.remove_task, text=REMOVE_TASK_BUTTON, font=buttons_font, background_color="#9562C4", foreground_color="white", active_background_color='#9562C4', position_options={"fill": "x"})
        self.order_task_button = Button()
        self.options_frame.add_widget(self.order_task_button)
        self.order_task_button.set_params(command=self.change_order, text=ORDER_TASK_BUTTON, font=buttons_font, background_color="#9562C4", foreground_color="white", active_background_color='#9562C4', position_options={"fill": "x"})
        self.complete_or_uncomplete_task_button = Button()
        self.options_frame.add_widget(self.complete_or_uncomplete_task_button)
        self.complete_or_uncomplete_task_button.set_params(command=self.complete_on_uncomplete_task, text=COMPLETE_OR_UNCOMPLETE_BUTTON, font=buttons_font, background_color="#9562C4", foreground_color="white", active_background_color='#9562C4', position_options={"fill": "x"})
        self.export_tasks_button = Button()
        self.options_frame.add_widget(self.export_tasks_button)
        self.export_tasks_button.set_params(command=self.export_tasks, text=EXPORT_BUTTON, font=buttons_font, background_color="#9562C4", foreground_color="white", active_background_color='#9562C4', position_options={"fill": "x"})
        self.quit_button = Button()
        self.options_frame.add_widget(self.quit_button)
        self.quit_button.set_params(command=self.program_exit, text=EXIT_BUTTON_TEXT, font=buttons_font, background_color="#9562C4", foreground_color="white", active_background_color='#9562C4', position_options={"side": "bottom", "fill": "x"})
        self.swap_theme_button = Button()
        self.options_frame.add_widget(self.swap_theme_button)
        self.swap_theme_button.set_params(command=self.swap_theme_mode, text=LIGHT_MODE_BUTTON, font=buttons_font, position_options={"side": "bottom", "fill": "x"})
    
    def create_widjets(self) -> None:
        self.create_window_widget()
        self.create_frame_widgets()
        self.create_text_widgets()
        self.create_label_widgets()
        self.create_button_widgets()
    
    def get_task_from_task_box(self) -> Task | None:
        task_text = self.task_box.tk_object.get("1.0", END).replace("\n", "")
        self.task_box.tk_object.delete("1.0", END)
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
            self.swap_theme_button._tk_object["text"] = DARK_MODE_BUTTON
        else:
            self.set_light_mode()
            self.swap_theme_button._tk_object["text"] = LIGHT_MODE_BUTTON
    
    def set_dark_mode(self) -> None:
        self.title._tk_object["fg"] = "black"
        self.tasks_frame._tk_object["bg"] = "black"
        self.tasks_list._tk_object["bg"] = "black"
        self.tasks_list._tk_object["fg"] = "white"
        self.current_theme = Themes.DARK_MODE
    
    def set_light_mode(self) -> None:
        self.title._tk_object["fg"] = "white"
        self.tasks_frame._tk_object["bg"] = "#f0f0f0"
        self.tasks_list._tk_object["bg"] = "#f0f0f0"
        self.tasks_list._tk_object["fg"] = "black"
        self.current_theme = Themes.LIGHT_MODE
