from typing import List, Union, Any

def flatten_array(arr: Union[List, Any]) -> List:
    """
    Recursively flatten a nested list into a single-level list.
    
    Args:
        arr (Union[List, Any]): Input list or nested list to be flattened.
    
    Returns:
        List: A flattened list containing all non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
        >>> flatten_array([])
        []
    """
    # Base case: if input is not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]
    
    # Recursive case: flatten each element and combine
    flattened = []
    for item in arr:
        # Recursively flatten each item and extend the result
        flattened.extend(flatten_array(item))
    
    return flattened