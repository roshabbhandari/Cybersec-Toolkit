"""UTC timestamp helpers for reports."""
from datetime import datetime, timezone

class TimeUtils:
    @staticmethod
    def utc_iso() -> str:
        return datetime.now(timezone.utc).isoformat()
