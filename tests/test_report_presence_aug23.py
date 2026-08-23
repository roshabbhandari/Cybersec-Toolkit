from core.report_presence import has_value


def test_has_value():
    assert has_value(0) is True
    assert has_value("") is False
    assert has_value(None) is False
