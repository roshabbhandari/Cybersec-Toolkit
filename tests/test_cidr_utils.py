from core.cidr_utils import CIDRUtils

def test_membership():
    assert CIDRUtils.contains("10.0.0.0/8", "10.1.2.3")
