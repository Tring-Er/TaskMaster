"""Contains CLI class"""


class CLI:
    """This class interact with the console"""

    @staticmethod
    def print_message(message: str) -> None:
        """It prints the message passed

        Args:
            message (str): the message to print
        """
        print(message)

    @staticmethod
    def input_message() -> str:
        """Return the input passed in the console by user

        Returns:
            str: The string inserted by user
        """
        return input()
