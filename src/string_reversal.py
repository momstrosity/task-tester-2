def reverse_string(input_string: str) -> str:
    """
    Reverse the given input string using a manual character-by-character approach.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Manual string reversal using list-based approach
    reversed_chars = []
    for char in input_string:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)