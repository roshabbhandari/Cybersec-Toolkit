"""Stable ordering helper for report mappings."""

def sort_report_keys(data: dict) -> dict:
    return {key: data[key] for key in sorted(data, key=lambda item: str(item).lower())}
