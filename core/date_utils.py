"""Date helpers used by reports."""
from datetime import datetime, timezone

class DateUtils:
    @staticmethod
    def utc_iso() -> str:
        return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
