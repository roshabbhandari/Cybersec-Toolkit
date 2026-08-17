from core.hash_generator import HashGenerator

def test_sha512_length():
    assert len(HashGenerator.text("x", "sha512")) == 128
