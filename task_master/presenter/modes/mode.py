"""Contains the abstract class for the mode with the action to perform"""

from abc import ABC, abstractmethod

from presenter.presenter import Presenter


class Mode(ABC):
    """The action to perform
    Every Mode MUST have a CLI_COMMAND public field that represent the command put in the
    CLI matched with the class
    """

    CLI_COMMAND: str

    @staticmethod
    @abstractmethod
    def execute(presenter: Presenter) -> None:
        """Execute the action based on the Action object

        Args:
            presenter (Presenter): The presenter class with the model and veiw
        """
