"""Canonical report status values."""

VALID_STATUSES = ("pass", "warn", "fail", "info")

def normalize_status(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("status must be a string")
    value = value.strip().lower()
    return value if value in VALID_STATUSES else "info"
