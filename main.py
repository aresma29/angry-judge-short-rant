#!/usr/bin/env python3
"""Print the short rant stored in entry.txt.

The rant lives in a sibling text file so the program itself stays small:
load it as UTF-8, trim the surrounding whitespace, and print it out.
"""

from pathlib import Path


def main() -> int:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
