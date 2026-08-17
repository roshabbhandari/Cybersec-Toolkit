"""Human-readable byte size formatting."""

class ByteSize:
    @staticmethod
    def human(value: int) -> str:
        value = int(value)
        units = ("B", "KiB", "MiB", "GiB", "TiB")
        size = float(value)
        for unit in units:
            if abs(size) < 1024 or unit == units[-1]:
                return f"{size:.2f} {unit}"
            size /= 1024
