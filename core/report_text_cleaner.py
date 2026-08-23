"""Normalize whitespace in report text."""

def clean_report_text(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return " ".join(value.split())
