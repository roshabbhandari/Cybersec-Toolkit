from core.aug22_none_default import default_when_none

def test_default_when_none():
    assert default_when_none(None, "x") == "x"
    assert default_when_none("y", "x") == "y"
