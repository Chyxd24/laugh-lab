"""Laugh Lab entry."""
import os

ENTRY = "The sock had it coming — it kept leaving itself where I walk, so I swallowed the evidence and called it deep cleaning."


def build_line() -> str:
    return ENTRY


def write_entry(path: str = "/output/entry.txt") -> tuple:
    line = build_line()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path, len(line)


if __name__ == "__main__":
    path, n = write_entry()
    print(f"wrote {n} chars to {path}")
