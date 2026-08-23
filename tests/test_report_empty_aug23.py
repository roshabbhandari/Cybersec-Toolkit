from core.report_empty import is_empty_report


def test_is_empty_report():
    assert is_empty_report(None) is True
    assert is_empty_report([]) is True
    assert is_empty_report({"x": 1}) is False
