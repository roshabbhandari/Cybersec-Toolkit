from core.hash_generator import HashGenerator

def test_empty_sha256_is_deterministic():
    assert HashGenerator.text("", "sha256") == HashGenerator.text("", "sha256")
