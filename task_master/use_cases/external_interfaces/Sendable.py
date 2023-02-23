"""A generic object that can be used to send data to"""


from abc import ABC, abstractmethod

from entities.Task import Task


class Sendable(ABC):
    
    @abstractmethod
    def send(self, tasks: list[Task]) -> None:
        """Sends a list of tasks object ot of the use_case"""