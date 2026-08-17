from core.jwt_decoder import JWTDecoder

def test_invalid_jwt_returns_error():
    result = JWTDecoder.decode("not-a-jwt")
    assert result.get("error")
