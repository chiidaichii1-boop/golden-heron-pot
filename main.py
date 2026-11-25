#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single fortune line (1-120 chars) to entry.txt in the output
directory. Stdlib only; no network, no randomness, no timestamps.
"""

import os

# The fortune: a prediction with a gentle twist — the "tall stranger in a
# yellow hat" is the morning sun, visiting the plant on the windowsill.
# Verified length: 97 characters (gate is 1-120).
ENTRY = "A tall stranger in a yellow hat will visit you every morning, ask nothing, and leave you glowing."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry length {len(text)} outside 1-120"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
