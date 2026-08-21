import pytest
from core.status_text import StatusText


def test_status_text():
    assert StatusText.normalize(" WARN ") == "warn"
    with pytest.raises(ValueError):
        StatusText.normalize("unknown")
