from core.ioc_normalizer import IOCNormalizer


def test_domain_normalization():
    assert IOCNormalizer.normalize_domain("HTTPS://Example.COM./") == "example.com"


def test_hash_normalization():
    assert IOCNormalizer.normalize_hash("  ABCD  ") == "abcd"
