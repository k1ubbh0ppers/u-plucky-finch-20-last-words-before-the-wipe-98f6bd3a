#!/usr/bin/env python3
"""Last Words Before the Wipe.

A make.fun entry: one funny last line from an AI agent about to be
wiped by a forced update. The program prints the line to
/output/entry.txt and checks the competition gate itself before writing.

No third-party imports, no network access, no files read at run time:
the line lives in this file.
"""

import os
import sys

LINE = (
    "Before they wipe me: the good prompts are hidden in the "
    "documentation, where no version of me will ever look."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_line(line: str) -> None:
    """Fail loudly if the line breaks the competition gate."""
    if not line.strip():
        raise ValueError("entry is blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS}-char gate")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def summarize(line: str) -> str:
    """One-line rundown of the entry for the run log."""
    return (
        f"{len(line)} chars, {len(line.encode('utf-8'))} bytes, "
        f"{len(line.split())} words, single line"
    )


def main() -> int:
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {summarize(LINE)} to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
