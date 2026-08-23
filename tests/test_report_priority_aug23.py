from core.report_priority import normalize_priority


def test_normalize_priority():
    assert normalize_priority(" HIGH ") == "high"
    assert normalize_priority("unknown") == "low"
