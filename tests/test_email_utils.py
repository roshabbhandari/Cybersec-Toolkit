from core.email_utils import EmailUtils

def test_valid_email():
    assert EmailUtils.is_valid("user@example.com")

def test_invalid_email():
    assert not EmailUtils.is_valid("invalid-email")
