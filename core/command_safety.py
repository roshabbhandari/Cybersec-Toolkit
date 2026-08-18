"""Basic safeguards for user-supplied local command names."""
import re

_SAFE_COMMAND = re.compile(r"^[A-Za-z0-9_.-]+$")


def is_safe_command_name(value: str) -> bool:
    return bool(isinstance(value, str) and value and _SAFE_COMMAND.fullmatch(value))
