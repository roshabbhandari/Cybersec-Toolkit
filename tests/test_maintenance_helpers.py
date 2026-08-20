from core.hostname_utils import HostnameUtils
from core.port_utils import PortUtils
from core.report_fields import ReportFields

def test_maintenance_helpers_smoke():
    assert HostnameUtils.normalize("EXAMPLE.COM.") == "example.com"
    assert PortUtils.validate(443) == 443
    assert ReportFields.normalize("IP") == "ip_address"
