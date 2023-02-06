"""This module contains a Button widget"""


from tkinter import Button as TkButton, Misc

from view.gui_widgets.widget import Widget


class Button(Widget):
    """GUI of a button widget"""

    def __init__(self) -> None:
        self.__button = TkButton()

    def ger_inner_object(self) -> Misc:
        return self.__button

    def set_text(self, text: str) -> None:
        """Set the button text"""

        self.__button.text = text

    def set_function(self, function: callable) -> None:
        """Set the function to perform once the button is pressed"""

        self.__button["command"] = function

    def set_parent(self, parent: Widget) -> None:
        """Set the parent of the widget"""

        self.__button.master = parent.ger_inner_object()

    def show(self) -> None:
        """Show the Button in the parent object"""

        self.__button.pack()
