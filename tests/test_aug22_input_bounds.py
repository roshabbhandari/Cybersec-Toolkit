from core.aug22_input_bounds import clamp_int


def test_clamp_int():
    assert clamp_int(9, 1, 5) == 5
    assert clamp_int(3, 1, 5) == 3
