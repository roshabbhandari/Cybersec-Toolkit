"""Create bounded previews for report output."""

class TextPreview:
    @staticmethod
    def limit(value: str, maximum: int = 120) -> str:
        if maximum < 0:
            raise ValueError("maximum must be non-negative")
        if len(value) <= maximum:
            return value
        if maximum <= 3:
            return value[:maximum]
        return value[: maximum - 3] + "..."
