def extract_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read().strip()