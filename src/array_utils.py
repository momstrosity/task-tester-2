from typing import List, Union, Any

def flatten_array(arr: List[Any]) -> List[Any]:
    """
    Recursively flatten a nested array of arbitrary depth into a single-level array.
    
    Args:
        arr (List[Any]): Input array that may contain nested arrays
    
    Returns:
        List[Any]: A flattened list containing all elements
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
    """
    flattened = []
    
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            # If not a list, add the item directly
            flattened.append(item)
    
    return flattened