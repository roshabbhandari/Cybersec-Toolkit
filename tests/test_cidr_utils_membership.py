from core.cidr_utils import CIDRUtils


def test_cidr_utils_reports_membership_for_ipv4_network():
    assert CIDRUtils.contains("192.0.2.0/24", "192.0.2.42") is True
    assert CIDRUtils.contains("192.0.2.0/24", "198.51.100.42") is False
