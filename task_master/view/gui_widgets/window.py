"""This module contains the GUI object"""


from tkinter import Tk, Misc

from view.gui_widgets.widget import Widget


class Window(Widget):
    """Window object"""

    def __init__(self) -> None:
        self.__window = Tk()

    def ger_inner_object(self) -> Misc:
        return self.__window

    def show_window(self) -> None:
        """Run the window object"""

        self.__window.mainloop()
