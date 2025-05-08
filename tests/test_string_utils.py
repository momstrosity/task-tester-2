import pytest
from src.string_utils import reverse_string

def test_reverse_normal_string():
    """Test reversal of a normal string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    """Test reversal of an empty string."""
    assert reverse_string("") == ""

def test_reverse_special_characters():
    """Test reversal of string with special characters."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_unicode_string():
    """Test reversal of unicode string."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_reverse_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list"])