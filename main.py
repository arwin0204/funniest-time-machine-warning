"""Funniest Time Machine Warning Label — one-line warning label entry.

Writes a single original one-line warning label for a time machine
(at most 120 characters) to entry.txt in the output directory.

Deterministic, no network, no secrets, no input files.

The joke's angle is deliberate: it turns a real hazard of time travel —
the grandfather paradox — into the punchline, phrased with a straight
face like a genuine safety notice, with the surprise saved for the last
few words ("He is load-bearing."). No wasted words.
"""

import os

ENTRY = "WARNING: Never introduce yourself to your grandfather. He is load-bearing."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_PATH") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
