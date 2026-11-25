#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single roast of a smart fridge to /output/entry.txt.

The roast: a 3am firmware update holds the ice maker hostage behind a
new terms-of-service screen. Concrete scene (3am update), one reversal
(the fridge, not the owner, sets the terms), one landing line.
Fridge-specific (firmware + ice maker), and it dodges the obvious
cracks — no grocery-ordering, no watching-you gag.
Standard library only.
"""

import os
import sys

ENTRY = (
    "My fridge pushed a firmware update at 3am, and now the ice maker "
    "won't drop a single cube until I accept the new terms of service."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"gate: entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
