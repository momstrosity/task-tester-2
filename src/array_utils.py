from typing import List, Union, Any

def flatten_array(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested list/array into a single-level list.
    
    Args:
        arr (Union[List[Any], Any]): The input array to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Raises:
        TypeError: If the input is not a list or does not support iteration.
    """
    # Base case: if input is not a list or is a string, return as single-element list
    if not isinstance(arr, list) or isinstance(arr, str):
        return [arr]
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # Recursively flatten each item and extend the result
        flattened.extend(flatten_array(item))
    
    return flattened