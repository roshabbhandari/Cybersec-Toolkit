from core.aug22_text_limits import limit_text


def test_limit_text():
    assert limit_text("abcdef", 4) == "abcd..."
    assert limit_text("abc", 4) == "abc"
