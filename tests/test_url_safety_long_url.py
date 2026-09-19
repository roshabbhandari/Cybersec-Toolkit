from core.url_safety import URLSafety


def test_url_safety_flags_unusually_long_urls():
    result = URLSafety.inspect("https://example.com/" + "a" * 181)
    assert result["suspicious"] is True
    assert "unusually long URL" in result["flags"]
