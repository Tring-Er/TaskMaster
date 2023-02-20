"""A generic object that can be read to obtain data"""


from abc import ABC, abstractmethod

from entities.Task import Task


class Readable(ABC):
    
    @abstractmethod
    def read(self) -> list[Task]:
        """Read tasks from outside the use_cases"""