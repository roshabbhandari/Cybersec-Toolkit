"""Basic email-like input validation for reports and metadata."""
import re

class EmailUtils:
    PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

    @staticmethod
    def is_valid(value: str) -> bool:
        return isinstance(value, str) and bool(EmailUtils.PATTERN.fullmatch(value.strip()))
