"""Dependency-free CSV export for security findings."""
import csv
from pathlib import Path

class CSVExporter:
    @staticmethod
    def save(rows, path: str) -> str:
        rows = list(rows)
        target = Path(path)
        if not rows:
            target.write_text("", encoding="utf-8")
            return str(target)
        with target.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader(); writer.writerows(rows)
        return str(target)
