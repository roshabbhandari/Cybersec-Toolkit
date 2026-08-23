"""Normalize human-readable report labels."""

def normalize_label(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("label must be a string")
    return " ".join(value.strip().replace("_", " ").split()).title()
