import pytest
from core.report_text_cleaner import clean_report_text


def test_clean_report_text():
    assert clean_report_text("  hello   world ") == "hello world"


def test_clean_report_text_type():
    with pytest.raises(TypeError):
        clean_report_text(123)
