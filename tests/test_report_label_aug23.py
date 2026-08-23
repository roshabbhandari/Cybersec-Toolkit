from core.report_label import normalize_label


def test_normalize_label():
    assert normalize_label("  risk_level  ") == "Risk Level"
