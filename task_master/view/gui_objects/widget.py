"""This abstract class containg a generic widget object"""


from abc import ABC, abstractmethod
from tkinter import Misc


class Widget(ABC):
    """An abstract class representing a generic GUI object"""

    @abstractmethod
    def ger_inner_object(self) -> Misc:
        """Used to get the object that manage the GUI (usually it's an external library object)"""
