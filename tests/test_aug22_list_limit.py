import pytest
from core.aug22_list_limit import limit_items

def test_limit_items():
    assert limit_items([1, 2, 3], 2) == [1, 2]

def test_negative_limit():
    with pytest.raises(ValueError):
        limit_items([1], -1)
