from core.text_redactor import TextRedactor

def test_redacts_api_key():
    assert "secret" not in TextRedactor.redact("api_key=secret")
