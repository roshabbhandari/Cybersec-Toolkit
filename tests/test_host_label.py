from core.host_label import HostLabel


def test_host_label_is_stable():
    assert HostLabel.make(" Example.COM. ") == "example.com"
    assert HostLabel.make("   ") == "unknown-host"
