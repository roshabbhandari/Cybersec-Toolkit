from core.report_status import normalize_status


def test_normalize_status():
    assert normalize_status(" WARN ") == "warn"
    assert normalize_status("unknown") == "info"
