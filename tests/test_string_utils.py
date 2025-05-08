import pytest
from src.string_utils import reverse_string

def test_reverse_standard_string():
    """Test reversing a standard ASCII string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_unicode_string():
    """Test reversing a string with unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"
    assert reverse_string("Hello, 世界!") == "!界世 ,olleH"

def test_reverse_palindrome():
    """Test reversing a palindrome."""
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("12321") == "12321"

def test_reverse_with_spaces_and_punctuation():
    """Test reversing strings with spaces and punctuation."""
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("a,b,c") == "c,b,a"

def test_invalid_input_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        reverse_string(12345)
    
    with pytest.raises(TypeError):
        reverse_string(None)
    
    with pytest.raises(TypeError):
        reverse_string(["hello"])