import json
from core.report_exporter import ReportExporter

def test_json_report_export(tmp_path):
    path = tmp_path / "report.json"
    ReportExporter.save({"status": "ok"}, str(path))
    assert json.loads(path.read_text(encoding="utf-8"))["status"] == "ok"
