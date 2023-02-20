"""This file contains a Task object that represent a task inside the program"""

class Task:
    """This is how tasks will be represented inside the project"""

    def __init__(self, text: str, is_completed: bool = False) -> None:
        self._text = text
        self._is_completed = is_completed
    
    @property
    def text(self) -> str:
        return self._text
    
    @property
    def is_completed(self) -> bool:
        return self._is_completed
    
    def complete(self) -> None:
        """Set the Task as completed"""

        self._is_completed = True
    
    def uncomplete(self) -> None:
        """Set the Task as not completed"""

        self._is_completed = False
