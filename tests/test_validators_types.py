import pytest
from core.validators import require_non_empty


def test_validator_rejects_none():
    with pytest.raises(ValueError):
        require_non_empty(None)
