"""Redact common secret-like values from logs and reports."""
import re


class TextRedactor:
    PATTERNS = [
        (re.compile(r"(?i)(api[_-]?key\s*[:=]\s*)[^\s,]+"), r"\1[REDACTED]"),
        (re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s]+"), r"\1[REDACTED]"),
        (re.compile(r"(?i)(password\s*[:=]\s*)[^\s,]+"), r"\1[REDACTED]"),
    ]

    @classmethod
    def redact(cls, text: str) -> str:
        for pattern, replacement in cls.PATTERNS:
            text = pattern.sub(replacement, text)
        return text
