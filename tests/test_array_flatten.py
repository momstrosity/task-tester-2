import pytest
from src.array_flatten import flatten_array

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_single_level_array():
    """Test flattening an already flat array."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_simple_nested_array():
    """Test flattening a simply nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], [5, 6]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_nested_array():
    """Test flattening an array with various nesting levels."""
    assert flatten_array([1, [2, 3, [4, 5]], 6, [7, [8, 9]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_flatten_array_with_different_types():
    """Test flattening an array with different types of elements."""
    assert flatten_array([1, ['a', 'b'], [2, ['c']]]) == [1, 'a', 'b', 2, 'c']