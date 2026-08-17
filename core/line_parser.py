"""Generic key/value line parser for defensive logs."""

class LineParser:
    @staticmethod
    def key_value(line: str, separator="=") -> tuple[str, str] | None:
        if separator not in line:
            return None
        key, value = line.split(separator, 1)
        key, value = key.strip(), value.strip()
        return (key, value) if key else None
