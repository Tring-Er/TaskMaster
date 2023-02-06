"""This module contains the GUI object with all the gui widgets"""


from view.gui_widgets.button import Button
from view.gui_widgets.label import Label
from view.gui_widgets.window import Window


class GUI:
    """The object that takes responsability to create and manage GUI widget objects"""

    def __init__(self) -> None:
        self.__window = Window()

    def add_label(self, text: str) -> None:
        """Adds a label widget to the current window"""

        label = Label()
        label.set_text(text)
        label.set_parent(self.__window)
        label.show()

    def add_button(self, text: str, function: callable) -> None:
        """Adds a button widget to the current window"""

        button = Button()
        button.set_text(text)
        button.set_function(function)
        button.set_parent(self.__window)
        button.show()

    def run(self) -> None:
        """Run the window object by showing it"""

        self.__window.show_window()
