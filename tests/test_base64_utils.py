from core.base64_utils import Base64Utils

def test_round_trip():
    value = "security toolkit"
    assert Base64Utils.decode(Base64Utils.encode(value)) == value
