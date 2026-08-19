"""Small reusable validation helpers."""


def require_non_empty(value: str, field: str = "value") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value.strip()
