import os
from pathlib import Path

ENTRY_TEXT = "Good news: we've reproduced the problem, so now there are two."
MAXIMUM_CHARACTERS = 199


def validate_entry(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("The entry cannot be empty.")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("The entry must remain on one line.")
    if len(cleaned) > MAXIMUM_CHARACTERS:
        raise ValueError("The entry exceeds the character limit.")
    return cleaned


def entry_destination() -> Path:
    output_root = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    return output_root / "entry.txt"


def main() -> None:
    destination = entry_destination()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(validate_entry(ENTRY_TEXT), encoding="utf-8")


if __name__ == "__main__":
    main()
