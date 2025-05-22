import pytest
from src.string_utils import flatten_list

def test_flatten_simple_nested_list():
    """Test flattening a simple nested list"""
    nested_list = [1, [2, 3], 4]
    assert flatten_list(nested_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    nested_list = [1, [2, [3, 4]], 5, [6, [7, 8]]]
    assert flatten_list(nested_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_list([]) == []

def test_flatten_list_with_mixed_types():
    """Test flattening a list with mixed types and nesting"""
    nested_list = [1, 'a', [2, 'b', [3, 'c']], 4]
    assert flatten_list(nested_list) == [1, 'a', 2, 'b', 3, 'c', 4]

def test_flatten_single_level_list():
    """Test flattening a list that is already flat"""
    flat_list = [1, 2, 3, 4]
    assert flatten_list(flat_list) == [1, 2, 3, 4]

def test_flatten_list_with_nested_empty_lists():
    """Test flattening a list with nested empty lists"""
    nested_list = [1, [], [2, []], 3]
    assert flatten_list(nested_list) == [1, 2, 3]

def test_flatten_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_list("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_list(123)