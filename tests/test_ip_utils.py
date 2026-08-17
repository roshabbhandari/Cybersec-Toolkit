from core.ip_utils import IPUtils

def test_private_ipv4():
    assert IPUtils.classify("192.168.1.10")["private"] is True
