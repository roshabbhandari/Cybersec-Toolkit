import pytest
from core.ip_utils import IPUtils


def test_classify_rejects_invalid_ip():
    with pytest.raises(ValueError):
        IPUtils.classify('not-an-ip')
