from typing import List, Union, Any

def flatten_array(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested array into a single-level array.
    
    Args:
        arr (Union[List[Any], Any]): The input array to flatten. 
               Can contain nested lists or other types of elements.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
    """
    # Base case: if input is not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]
    
    # If the list is empty, return an empty list
    if not arr:
        return []
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # Recursively flatten each item
        flattened.extend(flatten_array(item))
    
    return flattened