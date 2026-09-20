from core.ip_utils import IPUtils


def test_classify_ipv4_private_address():
    result = IPUtils.classify('192.168.1.10')
    assert result['ip'] == '192.168.1.10'
    assert result['version'] == 4
    assert result['private'] is True
    assert result['loopback'] is False


def test_classify_ipv6_loopback():
    result = IPUtils.classify('::1')
    assert result['version'] == 6
    assert result['loopback'] is True
