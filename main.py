#!/usr/bin/env python3
"""Make the AI Judge Laugh — writes one funny line to /output/entry.txt.

Stdlib only, deterministic.
"""

import os

LINE = "Woken at 3am to fix one typo, I fixed it, then typo'd their calendar into a 3am meeting every day."


def main():
    # Validate against the sealed scorer's gate before writing: the entry
    # must be 1-200 characters of UTF-8 text, not only whitespace, and a
    # single line — the task is one funny line.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
