def reverse_string(input_string):
    """
    Reverse a given string using manual character iteration.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Manual string reversal
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    
    return reversed_str