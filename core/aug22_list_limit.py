"""Limit report collections without changing item order."""

def limit_items(items, maximum: int):
    if maximum < 0:
        raise ValueError("maximum must be non-negative")
    return list(items)[:maximum]
