"""Keep only requested keys from a mapping."""

def select_keys(data: dict, keys) -> dict:
    wanted = set(keys)
    return {key: value for key, value in data.items() if key in wanted}
