import pytest
from core.aug22_bool_parser import parse_bool


def test_parse_bool():
    assert parse_bool("yes") is True
    assert parse_bool("off") is False


def test_parse_bool_invalid():
    with pytest.raises(ValueError):
        parse_bool("maybe")
