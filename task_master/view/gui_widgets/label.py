"""This module contains a Label object"""


from tkinter import Label as TkLabel, Misc

from view.gui_widgets.widget import Widget


class Label(Widget):
    """A label containing text"""

    def __init__(self) -> None:
        self.__label = TkLabel()

    def ger_inner_object(self) -> Misc:
        return self.__label

    def set_parent(self, parent: Widget) -> None:
        """Set the master Widget"""

        self.__label.master = parent.ger_inner_object()

    def set_text(self, text: str) -> None:
        """Set text for the label widget"""

        self.__label["text"] = text

    def show(self) -> None:
        """Show the Label in the parent object"""

        self.__label.pack()
