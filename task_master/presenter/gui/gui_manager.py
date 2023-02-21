"""This module contains the GUI presenter"""


from view.gui import GUI
from presenter.presenter import Presenter


class GUIManager(Presenter):
    """This class manages and creates all the GUI windows for the project"""

    def __init__(self, view: GUI) -> None:
        self.__view = view

    def compute(self) -> None:
        """It runs the project using the GUI"""

        self.__view.run()
