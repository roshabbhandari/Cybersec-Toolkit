"""Text length helpers used by defensive reports."""

def limit_text(value: str, maximum: int = 200) -> str:
    if maximum < 0:
        raise ValueError("maximum must be non-negative")
    text = str(value)
    return text if len(text) <= maximum else text[:maximum] + "..."
