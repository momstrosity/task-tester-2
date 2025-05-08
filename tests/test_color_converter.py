import pytest
from src.color_converter import rgb_to_hex

def test_basic_rgb_to_hex_conversion():
    """Test basic RGB to hex conversion."""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'   # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_edge_case_values():
    """Test conversion with edge case values."""
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_intermediate_values():
    """Test conversion with intermediate color values."""
    assert rgb_to_hex(128, 128, 128) == '#808080'
    assert rgb_to_hex(17, 34, 51) == '#112233'

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, '0', 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, 0, '0')

def test_out_of_range_inputs():
    """Test error handling for out-of-range input values."""
    with pytest.raises(ValueError):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 0, 300)