"""Render short lists consistently in reports."""

class ListText:
    @staticmethod
    def render(values: list[str], empty: str = "none") -> str:
        clean = [str(v).strip() for v in values if str(v).strip()]
        return ", ".join(clean) if clean else empty
