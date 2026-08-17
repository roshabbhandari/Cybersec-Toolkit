from core.url_safety import URLSafety

def test_url_safety_rejects_non_http_scheme():
    result = URLSafety.inspect("ftp://example.com")
    assert result["scheme"] == "ftp"
