"""Check whether a report value is meaningful."""

def has_value(value) -> bool:
    return value is not None and value != "" and value != [] and value != {}
