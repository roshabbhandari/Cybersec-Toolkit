from core.token_preview import TokenPreview


def test_token_preview_hides_remainder():
    assert TokenPreview.preview("secret-token", 4) == "secr..."
    assert TokenPreview.preview("abc", 4) == "***"
