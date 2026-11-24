#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes a single word to /output/entry.txt: "Situationship".

Why this word: home Wi-Fi is a situationship — sometimes it's there,
sometimes it vanishes, and it never commits. Funny at once, true to how
home Wi-Fi actually behaves, and fresh enough to work as a network name.

Deterministic, standard library only, no network access. The output is
always the same single word, byte for byte, on every run.
"""

import os

WORD = "Situationship"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the word, no trailing newline: 13 bytes, 13 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
