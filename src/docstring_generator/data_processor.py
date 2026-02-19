"""Module for processing numerical and string data."""


def calculate_average(numbers: list) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters
    ----------
    numbers : list
        The list of numbers to average.

    Returns
    -------
    float
        The average value of the numbers.
    """
    return sum(numbers) / len(numbers)


class DataProcessor:
    """
    Handle data processing tasks.

    Parameters
    ----------
    data : list
        The list of data to process.
    """

    def __init__(self, data: list):
        """
        Initialize the DataProcessor with a dataset.

        Parameters
        ----------
        data : list
            The list of data to process.
        """
        self.data = data

    def process_item(self, item: str, index: int = 0):
        """
        Process a specific item from the dataset.

        Parameters
        ----------
        item : str
            The string item to process.
        index : int, optional
            The position of the item in the data (default is 0).

        Returns
        -------
        str
            The processed item.
        """
        return item.upper()
