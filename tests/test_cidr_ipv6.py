from core.cidr_utils import CIDRUtils

def test_ipv6_membership():
    assert CIDRUtils.contains("2001:db8::/32", "2001:db8::5")
