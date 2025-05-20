def reverse_string(input_string):
    """
    Reverse a given string manually, without using slice notation or reverse().
    
    Args:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for manual reversal
    chars = list(input_string)
    
    # Manual reversal using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)