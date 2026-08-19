from core.validators import require_non_empty


def test_validator_default_field_message():
    try:
        require_non_empty("")
    except ValueError as exc:
        assert "value" in str(exc)
