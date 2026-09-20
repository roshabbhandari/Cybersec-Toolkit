from core.hex_utils import HexUtils


def test_hex_utils_accepts_even_length_hex():
    assert HexUtils.is_hex(" 00aF ") is True


def test_hex_utils_rejects_odd_length_and_non_hex_values():
    assert HexUtils.is_hex("abc") is False
    assert HexUtils.is_hex("gg") is False
