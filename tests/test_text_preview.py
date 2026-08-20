import pytest
from core.text_preview import TextPreview

def test_preview_limits_text():
    assert TextPreview.limit("abcdefgh", 6) == "abc..."

def test_preview_rejects_negative_limit():
    with pytest.raises(ValueError):
        TextPreview.limit("abc", -1)
