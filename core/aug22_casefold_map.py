"""Case-insensitive lookup for report metadata."""

def get_casefold(mapping: dict, key: str, default=None):
    wanted = str(key).casefold()
    for item_key, value in mapping.items():
        if str(item_key).casefold() == wanted:
            return value
    return default
