from core.ip_utils import IPUtils

def test_ipv6_version():
    assert IPUtils.classify("2001:db8::1")["version"] == 6
