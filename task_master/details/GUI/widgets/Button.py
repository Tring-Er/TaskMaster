from tkinter import Button as TkButton

from details.gui.widgets.Widget import Widget
from details.gui.widgets.ChildWidget import ChildWidget
from details.gui.widgets.Font import Font


class Button(ChildWidget):
    
    def __init__(self) -> None:
        self._tk_type = TkButton
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
        command: callable = kwargs.get("command", None)
        text: str = kwargs.get("text", None)
        font: Font = kwargs.get("font", None)
        background_color: str = kwargs.get("background_color", None)
        foreground_color: str = kwargs.get("foreground_color", None)
        active_background_color: str = kwargs.get("active_background_color", None)
        self.position_options: dict[str: ...] = kwargs.get("position_options", None)
        self._tk_object: TkButton = self._tk_type(self.parent.tk_object)
        self.set_command(command)
        self.set_text(text)
        self.set_font(font)
        self.set_background_color(background_color)
        self.set_foreground_color(foreground_color)
        self.set_active_background_color(active_background_color)
    
    def show(self) -> None:
        if self.position_options is None:
            self._tk_object.pack()
        else:
            self._tk_object.pack(**self.position_options)
        for widget in self.widgets:
            widget.show()
    
    def set_parent(self, widget: Widget) -> None:
        self.parent = widget
    
    def set_background_color(self, background_color: str) -> None:
        self._tk_object.config(background=background_color)
    
    def set_foreground_color(self, foreground_color: str) -> None:
        self._tk_object.config(foreground=foreground_color)
    
    def set_text(self, text: str) -> None:
        self._tk_object.config(text=text)
    
    def set_command(self, command: callable) -> None:
        self._tk_object.config(command=command)
    
    def set_font(self, font: Font) -> None:
        self._tk_object.config(font=font.tk_object)
    
    def set_active_background_color(self, active_background_color: str) -> None:
        self._tk_object.config(activebackground=active_background_color)
