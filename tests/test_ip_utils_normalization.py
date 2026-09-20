from core.ip_utils import IPUtils


def test_ip_utils_normalizes_whitespace_and_classifies_ipv4():
    result = IPUtils.classify(" 192.0.2.10 ")
    assert result["ip"] == "192.0.2.10"
    assert result["version"] == 4
