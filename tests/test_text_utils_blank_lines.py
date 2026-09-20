import pytest

from core.text_utils import normalize_lines


def test_normalize_lines_drops_blank_lines_and_strips_text():
    assert normalize_lines("  first\n\n second \n\t") == ["first", "second"]


def test_normalize_lines_rejects_non_string_input():
    with pytest.raises(TypeError):
        normalize_lines(None)
