def reverse_string(input_str):
    """
    Reverse a given string manually, without using slice notation or reverse().
    
    Args:
        input_str (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for easier manipulation
    chars = list(input_str)
    
    # Manually reverse the list of characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters from both ends
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)