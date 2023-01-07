"""Constains an abstract class for presenters"""

from abc import ABC, abstractmethod

from model.task_manager import TaskManager
from view.cli import CLI


class Presenter(ABC):
    """A presenter class, every presenter must be a Presenter"""

    model: TaskManager
    view: CLI

    @abstractmethod
    def compute(self) -> None:
        """Execute commands based on the presenter"""
