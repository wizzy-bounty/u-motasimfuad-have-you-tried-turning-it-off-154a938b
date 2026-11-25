import os
from pathlib import Path

SUPPORT_LINE = "I've sent the verification code to the phone you reported stolen."
CHARACTER_LIMIT = 199


def checked_line() -> str:
    line = SUPPORT_LINE.strip()
    if not line:
        raise ValueError("support line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("support line must stay on one line")
    if len(line) > CHARACTER_LIMIT:
        raise ValueError("support line is too long")
    return line


def destination() -> Path:
    root = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    return root / "entry.txt"


def main() -> None:
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(checked_line(), encoding="utf-8")


if __name__ == "__main__":
    main()
