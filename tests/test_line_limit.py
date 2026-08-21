from core.line_limit import LineLimit


def test_line_limit_clamps():
    assert LineLimit.clamp(["a", "b", "c"], 2) == ["a", "b"]
