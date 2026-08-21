from core.report_title import ReportTitle


def test_report_title():
    assert ReportTitle.make("  Security   Audit ") == "Security Audit"
    assert ReportTitle.make("") == "Security Report"
