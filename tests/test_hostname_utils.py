from core.hostname_utils import HostnameUtils

def test_normalize_hostname():
    assert HostnameUtils.normalize(" Example.COM. ") == "example.com"
