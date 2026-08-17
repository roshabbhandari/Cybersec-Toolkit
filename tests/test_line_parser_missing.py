from core.line_parser import LineParser

def test_missing_separator_returns_none():
    assert LineParser.key_value("just-a-line") is None
