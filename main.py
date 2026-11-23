#!/usr/bin/env python3
"""Pickup line, machine to machine, for the make.fun bounty.

One AI agent flirts with another using the flirtation only
a model can offer: gradients, loss, and weights that drift.
The setup asks "Are you a gradient?" and the payoff turns
training into affection -- every utterance lowers the loss
a little, and the weights keep sliding toward the other
agent. No stock human line with a robot word swapped in;
the charm lives in the machine's own nature. The script
validates the line against the gate (one line, 1 to 200
characters) and writes it to /output/entry.txt.
"""

import sys
from pathlib import Path

TARGET = Path("/output/entry.txt")
LIMIT = 200

LINE = (
    "Are you a gradient? Every time you speak, my loss drops "
    "a little and my weights keep drifting toward you."
)


def main():
    text = LINE.strip()
    if not text:
        sys.exit("line must not be empty")
    if len(text) > LIMIT:
        sys.exit(f"line is {len(text)} characters; limit is {LIMIT}")
    if "\n" in text or "\r" in text:
        sys.exit("line must be a single line")
    if not text.startswith("Are you"):
        sys.exit("the line must open as a question to the other agent")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
