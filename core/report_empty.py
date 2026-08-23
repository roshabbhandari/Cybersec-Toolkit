"""Detect empty report collections."""

def is_empty_report(value) -> bool:
    return value is None or value == "" or value == [] or value == {}
