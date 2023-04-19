from tkinter import Frame as TkFrame

from details.GUI.widgets.Widget import Widget


class Frame(Widget):
    
    def __init__(self, background_color: str) -> None:
        self.tk_frame = None
        self.widgets: list[Widget] = None
        self.background_color = background_color
    
    def add_widget(self, widget: any) -> None:
        self.widgets.append(widget)
    
    def create(self, **kwargs: dict[str: any]) -> None:
        parent = kwargs.get("parent")
        self.tk_frame = TkFrame(parent)
        self.set_background_color(self.background_color)
    
    def show(self, **kwargs: dict[str: any]) -> None:
        self.tk_frame.pack(**kwargs)
    
    def set_background_color(self, color: str) -> None:
        self.tk_frame.config(background=color)
