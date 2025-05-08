import pytest
from src.array_utils import flatten_array

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_single_level_array():
    """Test flattening a single-level array."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_array():
    """Test flattening a nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], [5, 6]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_nested_array():
    """Test flattening an array with mixed nested levels."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_array_with_mixed_types():
    """Test flattening an array with mixed data types."""
    assert flatten_array([1, 'a', [2, 'b'], [3, [4, 'c']]]) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_single_element_nested_arrays():
    """Test flattening arrays with single-element nested arrays."""
    assert flatten_array([[1], [2], [3]]) == [1, 2, 3]

def test_complex_nested_structure():
    """Test a more complex nested array structure."""
    complex_array = [1, [2, 3, [4, 5]], 6, [7, [8, 9, [10]]]]
    assert flatten_array(complex_array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]