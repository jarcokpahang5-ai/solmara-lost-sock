"""Funniest Lost Sock Status Update — make.fun bounty entry
(u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce).

The joke: a lost sock posts a status update from its new home — the dog's
bed. The premise is clear (a sock somewhere it should not be), and the
punchline lands in the last few words: the dog, who snores and drools, is
a better partner than the foot the sock left behind. It twists the
obvious sock material — the missing partner — by replacing the partner
with the dog, and the foot with the one who got dumped.

Pure Python 3.13 standard library only. Deterministic, no network.
Writes the single entry line to /output/entry.txt and prints it to
stdout, byte-identical to the file (modulo the trailing newline).
"""

import os

ENTRY = (
    "Status: living in the dog's bed now. He snores, he drools — "
    "and honestly? He's a better partner than the foot I left."
)


def build_line() -> str:
    """Return the single status-update line (<= 120 characters)."""
    return ENTRY


def main() -> None:
    line = build_line()
    assert 1 <= len(line) <= 120, f"line is {len(line)} chars, must be 1-120"
    assert "\n" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
