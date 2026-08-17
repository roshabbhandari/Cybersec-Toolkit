from core.line_parser import LineParser

def test_key_value():
    assert LineParser.key_value("mode=safe") == ("mode", "safe")
