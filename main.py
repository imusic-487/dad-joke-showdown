#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.

The joke: a dad tells the dishwasher he loves it, and the dishwasher
answers with the pun -- "loading" as in loading the dishes, and as in
loading someone with your problems. One clean pun, spoken aloud at the
dinner table, punchline at the end.
"""

import os
import sys

JOKE = (
    "I told the dishwasher I loved it. "
    "It said, 'Thanks, but please stop loading me "
    "with all your problems.'"
)


def main() -> int:
    text = JOKE
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"joke is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(encoded)
    print(f"wrote {len(encoded)} bytes, {len(text)} characters to {out_path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
