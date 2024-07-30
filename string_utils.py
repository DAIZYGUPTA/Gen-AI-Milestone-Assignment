# 14. Implement a Python module named string_utils.py containing functions for string manipulation, such as reversing and capitalizing strings.

def reverse_string(s):
    """
    Reverses the given string.
    Parameters:
    s (str): The string to reverse.
    Returns:
    str: The reversed string.
    """
    return s[::-1]

def capitalize_string(s):
    """
    Capitalizes the first letter of each word in the given string.
    Parameters:
    s (str): The string to capitalize.
    Returns:
    str: The capitalized string.
    """
    return s.title()

def to_upper(s):
    """
    Converts all characters in the given string to uppercase.
    Parameters:
    s (str): The string to convert.
    Returns:
    str: The string in uppercase.
    """
    return s.upper()

def to_lower(s):
    """
    Converts all characters in the given string to lowercase.
    Parameters:
    s (str): The string to convert.
    Returns:
    str: The string in lowercase.
    """
    return s.lower()

def count_vowels(s):
    """
    Counts the number of vowels in the given string.
    Parameters:
    s (str): The string to count vowels in.
    Returns:
    int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """
    Checks if the given string is a palindrome.
    Parameters:
    s (str): The string to check.
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]
