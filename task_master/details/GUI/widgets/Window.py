from tkinter import Tk

from details.GUI.widgets.Widget import Widget


class Window(Widget):
    """Wrapper arround Tk object"""
    
    def __init__(self, title: str, icon_path: str, percentage_of_screen_width_taken_by_window: float, percentage_of_screen_height_taken_by_window: float) -> None:
        self.tk_object = None
        self.widgets: list[Widget] = []
        self.size = (percentage_of_screen_width_taken_by_window, percentage_of_screen_height_taken_by_window)
        self.title = title
        self.icon_path = icon_path
    
    def add_widget(self, widget: Widget) -> None:
        self.widgets.append(widget)
    
    def create(self, **kwargs: dict[str: any]) -> None:
        self.tk_object = Tk()
        self.set_geometry(*self.size)
        self.set_title(self.title)
        self.set_icon(self.icon_path)
        for widget in self.widgets:
            widget.create(parent=self.tk_object)
    
    def show(self) -> None:
        for widget in self.widgets:
            widget.show()
        self.tk_object.mainloop()
    
    def set_geometry(self, percentage_of_screen_width_taken_by_window: float, percentage_of_screen_height_taken_by_window: float) -> None:
        screen_width = self.tk_object.winfo_screenwidth()
        screen_height = self.tk_object.winfo_screenheight()
        window_width = int(screen_width * percentage_of_screen_width_taken_by_window)
        window_height = int(screen_height * percentage_of_screen_height_taken_by_window)
        x_coord = screen_width//2 - window_width//2
        y_coord = screen_height//2 - window_height//2
        centered_geometry = f"{window_width}x{window_height}+{x_coord}+{y_coord}"
        self.tk_object.geometry(centered_geometry)
    
    def set_title(self, title: str) -> None:
        self.tk_object.title(title)
    
    def set_icon(self, icon_path: str) -> None:
        self.tk_object.iconbitmap(icon_path)
