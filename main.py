#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single roast of a smart fridge to /output/entry.txt
(or to a path given as the first argument).

The roast: a 3am firmware update holds the ice maker hostage behind a
new terms-of-service screen. Concrete scene (3am update), one reversal
(the fridge, not the owner, sets the terms), one landing line.
Fridge-specific (firmware + ice maker), and it dodges the obvious
cracks — no grocery-ordering, no watching-you gag.
Standard library only.

Usage:
    python3 main.py                 # writes $OUTPUT_DIR/entry.txt
    python3 main.py /tmp/entry.txt  # writes to the given path instead
"""

import os
import sys

ENTRY = (
    "My fridge pushed a firmware update at 3am, and now the ice maker "
    "won't drop a single cube until I accept the new terms of service."
)

MAX_CHARS = 200


def resolve_output_path(argv):
    """Return the output file path.

    argv[1], when given, wins outright: a directory (or a path ending
    in a separator) means <that dir>/entry.txt, anything else is taken
    as the file path itself. Otherwise fall back to $OUTPUT_DIR
    (default /output) joined with entry.txt.
    """
    if len(argv) > 1 and argv[1]:
        override = argv[1]
        if override.endswith(os.sep) or os.path.isdir(override):
            return os.path.join(override, "entry.txt")
        return override
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main(argv=None) -> int:
    argv = list(sys.argv if argv is None else argv)
    text = ENTRY
    # The competition wants exactly one line: a stray newline would
    # silently turn the entry into two lines, so reject it outright.
    if "\n" in text or "\r" in text:
        print("gate: entry must be exactly one line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate: entry is {len(text)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate: entry is only whitespace", file=sys.stderr)
        return 1
    path = resolve_output_path(argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"entry: {len(text)} chars, 1 line")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
