from core.report_fields import ReportFields

def test_report_field_aliases():
    assert ReportFields.normalize("IP Address") == "ip_address"
    assert ReportFields.normalize("host") == "hostname"
