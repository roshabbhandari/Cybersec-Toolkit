from core.string_safety import StringSafety

def test_normalize_whitespace():
    assert StringSafety.normalize("  hello   world  ") == "hello world"
