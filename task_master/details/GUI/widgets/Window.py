from tkinter import Tk

from details.gui.widgets.Widget import Widget
from details.gui.widgets.ChildWidget import ChildWidget


class Window(Widget):
    """Wrapper arround Tk object"""
    
    def __init__(self) -> None:
        self._tk_type = Tk
        self.widgets: list[Widget] = []
    
    @property
    def tk_object(self) -> object:
        return self._tk_object
    
    def add_widget(self, widget: ChildWidget) -> None:
        widget.set_parent(self)
        self.widgets.append(widget)
    
    def set_graphics(self, **kwargs) -> None:
        title: str = kwargs.get("title", None)
        icon_path: str = kwargs.get("icon_path", None)
        percentage_of_screen_width_taken_by_window: float = kwargs.get("percentage_of_screen_width_taken_by_window", None)
        percentage_of_screen_height_taken_by_window: float = kwargs.get("percentage_of_screen_height_taken_by_window", None)
        self._tk_object: Tk = self._tk_type()
        self.set_geometry(percentage_of_screen_width_taken_by_window, percentage_of_screen_height_taken_by_window)
        self.set_title(title)
        self.set_icon(icon_path)
    
    def show(self) -> None:
        for widget in self.widgets:
            widget.show()
        self._tk_object.mainloop()
    
    def set_geometry(self, percentage_of_screen_width_taken_by_window: float, percentage_of_screen_height_taken_by_window: float) -> None:
        if percentage_of_screen_height_taken_by_window is None or percentage_of_screen_width_taken_by_window is None:
            return
        screen_width = self._tk_object.winfo_screenwidth()
        screen_height = self._tk_object.winfo_screenheight()
        window_width = int(screen_width * percentage_of_screen_width_taken_by_window)
        window_height = int(screen_height * percentage_of_screen_height_taken_by_window)
        x_coord = screen_width//2 - window_width//2
        y_coord = screen_height//2 - window_height//2
        centered_geometry = f"{window_width}x{window_height}+{x_coord}+{y_coord}"
        self._tk_object.geometry(centered_geometry)
    
    def set_title(self, title: str) -> None:
        self._tk_object.title(title)
    
    def set_icon(self, icon_path: str) -> None:
        self._tk_object.iconbitmap(icon_path)
