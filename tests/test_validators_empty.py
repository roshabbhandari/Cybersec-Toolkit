from core.validators import require_non_empty


def test_require_non_empty_strips_whitespace():
    assert require_non_empty("  ok  ") == "ok"
