import pytest
from core.base64_utils import Base64Utils

def test_invalid_base64_rejected():
    with pytest.raises(Exception):
        Base64Utils.decode("not valid base64!")
