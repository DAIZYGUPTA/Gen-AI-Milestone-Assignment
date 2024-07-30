# 15. Write a Python module named file_operations.py with functions for reading, writing, and appending data to a file.

def write_to_file(file_path, data):
    """
    Writes data to a file, overwriting the existing content.
    Parameters:
    file_path (str): The path to the file.
    data (str): The data to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(data)

def append_to_file(file_path, data):
    """
    Appends data to a file.
    Parameters:
    file_path (str): The path to the file.
    data (str): The data to append to the file.
    """
    with open(file_path, 'a') as file:
        file.write(data)

def read_from_file(file_path):
    """
    Reads data from a file.
    Parameters:
    file_path (str): The path to the file.
    Returns:
    str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()
