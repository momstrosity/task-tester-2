def reverse_string(input_string):
    """\n    Reverse a given string using manual character iteration.\n\n    Args:\n        input_string (str): The string to be reversed.\n\n    Returns:\n        str: The reversed string.\n\n    Raises:\n        TypeError: If the input is not a string.\n    """\n    # Check if input is a string\n    if not isinstance(input_string, str):\n        raise TypeError("Input must be a string")\n    \n    # Manual string reversal\n    reversed_str = ""\n    for char in input_string:\n        reversed_str = char + reversed_str\n    \n    return reversed_str

def rgb_to_hex(r, g, b):
    """
    Convert RGB color values to a hexadecimal color code.

    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)

    Returns:
        str: Hexadecimal color code (e.g., '#FF0000' for bright red)

    Raises:
        ValueError: If any color value is outside the range 0-255
        TypeError: If any input is not an integer
    """
    # Validate input types
    if not all(isinstance(x, int) for x in (r, g, b)):
        raise TypeError("RGB values must be integers")
    
    # Validate color values are within 0-255 range
    if not all(0 <= x <= 255 for x in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")
    
    # Convert to hex, ensuring two-digit representation
    hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
    
    return hex_color