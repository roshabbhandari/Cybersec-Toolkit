from core.csv_exporter import CSVExporter

def test_csv_export(tmp_path):
    path = tmp_path / "rows.csv"
    CSVExporter.save([{"name": "ok", "score": 1}], str(path))
    assert "name,score" in path.read_text(encoding="utf-8")
