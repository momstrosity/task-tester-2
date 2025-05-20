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
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if len(input_string) <= 1:
        return input_string
    
    # Convert string to list for manipulation
    chars = list(input_string)
    
    # Swap characters from start to end
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)