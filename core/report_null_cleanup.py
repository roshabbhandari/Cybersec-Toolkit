"""Report cleanup helper for removing None-valued fields."""

def drop_none_fields(data: dict) -> dict:
    return {key: value for key, value in data.items() if value is not None}
