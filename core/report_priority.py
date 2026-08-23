"""Canonical report priority normalization."""
PRIORITIES = ("low", "medium", "high", "critical")

def normalize_priority(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("priority must be a string")
    value = value.strip().lower()
    return value if value in PRIORITIES else "low"
