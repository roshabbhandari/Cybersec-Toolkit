"""Return a fallback when a value is None."""

def default_when_none(value, fallback):
    return fallback if value is None else value
