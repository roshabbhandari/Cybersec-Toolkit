from core.url_normalizer import URLNormalizer

def test_default_https_port_removed():
    assert URLNormalizer.normalize("https://example.com:443") == "https://example.com/"
