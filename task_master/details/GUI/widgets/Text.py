from tkinter import Text as TkText

from details.gui.widgets.ChildWidget import ChildWidget
from details.gui.widgets.Widget import Widget


class Text(ChildWidget):
    
    def __init__(self) -> None:
        self._tk_type = TkText
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
        height: int = kwargs.get("height", None)
        width: int = kwargs.get("width", None)
        self.position_options: dict[str: ...] = kwargs.get("position_options", None)
        self._tk_object: TkText = self._tk_type(self.parent.tk_object)
        self.set_height(height)
        self.set_width(width)
    
    def show(self) -> None:
        if self.position_options is None:
            self._tk_object.pack()
        else:
            self._tk_object.pack(**self.position_options)
        for widget in self.widgets:
            widget.show()
    
    def set_parent(self, widget: Widget) -> None:
        self.parent = widget
    
    def set_height(self, height: int) -> None:
        self._tk_object.config(height=height)
    
    def set_width(self, width: int) -> None:
        self._tk_object.config(width=width)
