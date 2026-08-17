from core.url_normalizer import URLNormalizer

def test_normalizes_host():
    assert URLNormalizer.normalize("EXAMPLE.COM") == "https://example.com/"
