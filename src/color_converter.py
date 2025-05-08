def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal color code.

    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)

    Returns:
        str: Hexadecimal color code (e.g., '#FF0000')

    Raises:
        ValueError: If any color value is not in the range 0-255
        TypeError: If color values are not integers
    """
    # Validate input types
    if not all(isinstance(x, int) for x in (r, g, b)):
        raise TypeError("RGB values must be integers")
    
    # Validate input ranges
    if not all(0 <= x <= 255 for x in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")
    
    # Convert to hex and ensure two-digit representation
    return f'#{r:02X}{g:02X}{b:02X}'