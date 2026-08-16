"""Simple JSON report exporter for defensive scan results."""
import json
from datetime import datetime, timezone
from pathlib import Path


class ReportExporter:
    @staticmethod
    def save(data: dict, path: str) -> str:
        output = Path(path)
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "tool": "Cybersec-Toolkit",
            "results": data,
        }
        output.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
        return str(output)
