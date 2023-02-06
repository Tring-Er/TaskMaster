"""This module contains the GUI presenter"""


from view.gui import GUI
from model.task_manager import TaskManager
from presenter.presenter import Presenter


class GUIManager(Presenter):
    """This class manages and creates all the GUI windows for the project"""

    def __init__(self, model: TaskManager, view: GUI) -> None:
        self.__model = model
        self.__view = view

    def compute(self) -> None:
        """It runs the project using the GUI"""

        self.__view.run()
