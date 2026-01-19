"""Module for processing numerical and string data."""


def calculate_average(numbers: list) -> float:
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)


class DataProcessor:
    """Handle data processing tasks."""

    def __init__(self, data: list):
        """Initialize the DataProcessor with a dataset.

        Args:
            data: The list of data to process.
        """
        self.data = data

    def process_item(self, item: str, index: int = 0):
        """Process a specific item from the dataset.

        Args:
            item: The string item to process.
            index: The position of the item in the data.
        """
        pass
