from core.empty_default import EmptyDefault


def test_empty_default():
    assert EmptyDefault.get(None) == "N/A"
    assert EmptyDefault.get("  ") == "N/A"
    assert EmptyDefault.get("value") == "value"
