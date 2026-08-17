from core.input_guard import InputGuard

def test_non_empty_strips():
    assert InputGuard.non_empty("  ok  ") == "ok"

def test_bounded_int():
    assert InputGuard.bounded_int(5, 1, 10) == 5
