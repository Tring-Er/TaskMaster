"""Constains an abstract class for presenters"""

from abc import ABC, abstractmethod


class Presenter(ABC):
    """A presenter class, every presenter must be a Presenter"""

    @abstractmethod
    def compute(self) -> None:
        """Execute commands based on the presenter"""
