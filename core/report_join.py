"""Join report text fragments consistently."""

def join_lines(lines) -> str:
    return "\n".join(str(line).strip() for line in lines if str(line).strip())
