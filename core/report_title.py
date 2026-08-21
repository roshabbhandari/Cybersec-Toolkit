"""Create compact, consistent report titles."""

class ReportTitle:
    @staticmethod
    def make(title: str) -> str:
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        value = " ".join(title.split())
        return value[:80] or "Security Report"
