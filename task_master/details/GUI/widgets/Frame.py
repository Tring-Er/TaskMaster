from tkinter import Frame as TkFrame

from details.GUI.widgets.Widget import Widget


class Frame(Widget):
    
    def __init__(self, background_color: str, **position_options: dict[str: any]) -> None:
        self.tk_object: TkFrame = None
        self.parent: Widget = None
        self.widgets: list[Widget] = None
        self.background_color = background_color
        self.position_options = position_options
    
    def add_widget(self, widget: Widget) -> None:
        self.widgets.append(widget)
        widget.set_parent(self.tk_object)
    
    def create(self, **kwargs: dict[str: any]) -> None:
        parent = kwargs.get("parent")
        self.tk_object = TkFrame(parent)
        self.set_background_color(self.background_color)
    
    def show(self) -> None:
        self.tk_object.pack(**self.position_options)
        for widget in self.widgets:
            widget.show()
    
    def set_background_color(self, color: str) -> None:
        self.tk_object.config(background=color)
