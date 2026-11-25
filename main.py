import os
from pathlib import Path

ENTRY = "For security, I've emailed the reset link to the inbox it unlocks."
MAX_CHARS = 199


def checked_entry() -> str:
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    return text


def output_path() -> Path:
    directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return directory / "entry.txt"


def write_entry() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(checked_entry(), encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
