# 📚 API Reference

This page documents the core components of the DocuGenius library.

## **Module: `data_processor.py`**
The main processing module for data handling and average calculations.

### `calculate_average(numbers)`
Calculates the arithmetic mean of a provided list.

* **Parameters:**
    * `numbers` (list): A list of numerical values.
* **Returns:**
    * `float`: The calculated average.

---

## **Class: `DataProcessor`**
A class-based handler for managing larger datasets.

### `__init__(self, data)`
Initializes the processor with a specific dataset.

* **Parameters:**
    * `data` (list): The list of data points to store.

### `process_item(self, item, index=0)`
Transforms a specific string item from the dataset to uppercase.

* **Parameters:**
    * `item` (str): The string to process.
    * `index` (int, optional): The position in the dataset.
* **Returns:**
    * `str`: The item in uppercase format.

---

## **UI Engine: `app.py`**
The Streamlit-based interface for interactive docstring auditing.

* **Key Features:**
    * **AST Integration**: Parses Python files into an Abstract Syntax Tree for audit.
    * **PEP-257 Validator**: Cross-references components against pydocstyle rules.
# 📚 API Reference

::: docstring_generator.data_processor
::: docstring_generator.app