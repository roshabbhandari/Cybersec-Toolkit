from core.text_redactor import TextRedactor

def test_redacts_bearer_token():
    output = TextRedactor.redact("Authorization: Bearer abc123")
    assert "abc123" not in output
