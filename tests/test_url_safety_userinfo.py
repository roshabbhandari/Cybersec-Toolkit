from core.url_safety import URLSafety


def test_url_safety_flags_userinfo_urls():
    result = URLSafety.inspect("https://user@example.com/login")
    assert result["suspicious"] is True
    assert "userinfo in URL" in result["flags"]
