"""Contains class TaskManager"""


class TaskManager:
    """
    Manages tasks
    It's an interface on top of other objects
    """
    @staticmethod
    def task(message: str) -> str:
        """Returns the exact message sent

        Args:
            message (str): the task

        Returns:
            str: the task
        """
        return message
