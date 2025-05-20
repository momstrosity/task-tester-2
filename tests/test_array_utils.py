import pytest
from src.array_utils import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_multiple_levels_of_nesting():
    """Test flattening multiple levels of nested lists"""
    nested = [1, [2, [3, [4, 5]]], 6]
    assert flatten_array(nested) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types"""
    mixed = [1, 'a', [2, [3.14]], {'key': 'value'}]
    assert flatten_array(mixed) == [1, 'a', 2, 3.14, {'key': 'value'}]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_flatten_non_nested_element():
    """Test flattening a non-nested element"""
    assert flatten_array(42) == [42]

def test_flatten_string():
    """Test that strings are treated as single elements"""
    assert flatten_array('hello') == ['hello']