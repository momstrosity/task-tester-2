import pytest
from src.string_utils import rgb_to_hex, reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    with pytest.raises(TypeError):
        reverse_string(123)

def test_rgb_to_hex_basic_conversion():
    """Test basic RGB to hex conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Bright Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Bright Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Bright Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'   # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_rgb_to_hex_mixed_colors():
    """Test conversion of mixed color values"""
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Mid Gray
    assert rgb_to_hex(100, 200, 50) == '#64C832'  # Mixed color

def test_rgb_to_hex_type_errors():
    """Test type validation for inputs"""
    with pytest.raises(TypeError):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, '0', 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, 0, '0')
    with pytest.raises(TypeError):
        rgb_to_hex(255.5, 0, 0)

def test_rgb_to_hex_value_errors():
    """Test value range validation"""
    with pytest.raises(ValueError):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 0, 300)