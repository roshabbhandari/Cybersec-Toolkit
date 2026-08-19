import pytest
from core.validators import require_non_empty


def test_validator_message_has_field_name():
    with pytest.raises(ValueError, match="username"):
        require_non_empty("", "username")
