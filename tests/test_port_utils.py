import pytest
from core.port_utils import PortUtils

def test_valid_port():
    assert PortUtils.validate(443) == 443

def test_invalid_port():
    with pytest.raises(ValueError):
        PortUtils.validate(70000)
