import pytest
from src.array_utils import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_mixed_content():
    """Test flattening a list with mixed content types."""
    assert flatten_array([1, 'a', [2, ['b']], 3]) == [1, 'a', 2, 'b', 3]

def test_flatten_single_item():
    """Test flattening a single item."""
    assert flatten_array(42) == [42]

def test_flatten_nested_empty_lists():
    """Test flattening list with nested empty lists."""
    assert flatten_array([[], [1, []], 2]) == [1, 2]