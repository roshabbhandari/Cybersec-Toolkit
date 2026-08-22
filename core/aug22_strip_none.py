"""Remove None-valued fields from report mappings."""

def drop_none(data: dict) -> dict:
    return {key: value for key, value in data.items() if value is not None}
