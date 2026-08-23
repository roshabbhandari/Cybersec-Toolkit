import pytest
from core.report_limit import limit_items


def test_limit_items():
    assert limit_items([1, 2, 3], 2) == [1, 2]


def test_limit_items_rejects_negative():
    with pytest.raises(ValueError):
        limit_items([1], -1)
