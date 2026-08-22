"""Small defensive bounds helpers for CLI input."""

def clamp_int(value: int, minimum: int, maximum: int) -> int:
    if minimum > maximum:
        raise ValueError("minimum cannot exceed maximum")
    return max(minimum, min(maximum, int(value)))
