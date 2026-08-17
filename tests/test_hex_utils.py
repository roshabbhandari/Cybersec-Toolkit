from core.hex_utils import HexUtils

def test_valid_hex():
    assert HexUtils.is_hex("00ffAA")

def test_odd_length_is_invalid():
    assert not HexUtils.is_hex("abc")
