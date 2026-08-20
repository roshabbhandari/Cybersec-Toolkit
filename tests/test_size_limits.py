import pytest
from core.size_limits import SizeLimits

def test_clamp_bounds():
    assert SizeLimits.clamp(5, 1, 10) == 5
    assert SizeLimits.clamp(0, 1, 10) == 1
    assert SizeLimits.clamp(20, 1, 10) == 10

def test_invalid_bounds():
    with pytest.raises(ValueError):
        SizeLimits.clamp(5, 10, 1)
