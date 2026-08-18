import pytest

from core.text_utils import normalize_lines


def test_normalize_lines():
    assert normalize_lines("  one\n\n two  \n") == ["one", "two"]


def test_normalize_lines_type_error():
    with pytest.raises(TypeError):
        normalize_lines(None)
