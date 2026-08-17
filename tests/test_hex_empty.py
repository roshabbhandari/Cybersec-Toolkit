from core.hex_utils import HexUtils

def test_empty_hex_is_invalid():
    assert not HexUtils.is_hex("")
