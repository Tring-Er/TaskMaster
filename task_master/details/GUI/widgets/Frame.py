from tkinter import Frame as TkFrame

from details.gui.widgets.ChildWidget import ChildWidget
from details.gui.widgets.Widget import Widget


class Frame(ChildWidget):
    
    def __init__(self) -> None:
        self._tk_type = TkFrame
        self.parent: Widget = None
        self.widgets: list[Widget] = []
        self.position_options = None
    
    @property
    def tk_object(self) -> object:
        return self._tk_object
    
    def add_widget(self, widget: ChildWidget) -> None:
        widget.set_parent(self)
        self.widgets.append(widget)
    
    def set_params(self, **kwargs) -> None:
        background_color: str = kwargs.get("background_color", None)
        self.position_options: dict[str: ...] = kwargs.get("position_options", None)
        self._tk_object: TkFrame = self._tk_type(self.parent.tk_object)
        self.set_background_color(background_color)
    
    def show(self) -> None:
        if self.position_options is None:
            self._tk_object.pack()
        else:
            self._tk_object.pack(**self.position_options)
        for widget in self.widgets:
            widget.show()
    
    def set_parent(self, widget: Widget) -> None:
        self.parent = widget
    
    def set_background_color(self, color: str) -> None:
        self._tk_object.config(background=color)
