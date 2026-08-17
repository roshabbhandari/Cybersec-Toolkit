import pytest
from core.input_guard import InputGuard

def test_empty_rejected():
    with pytest.raises(ValueError):
        InputGuard.non_empty("   ")

def test_out_of_range_rejected():
    with pytest.raises(ValueError):
        InputGuard.bounded_int(11, 1, 10)
