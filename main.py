#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh: Office Jokes" bounty.

Writes one line -- a single joke about office life -- to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

JOKE = "I asked for a raise and got a standing desk. Technically, I did rise."


def main():
    # Fail fast if the line ever stops satisfying the gate
    # (UTF-8, 1-200 chars, not only whitespace).
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise SystemExit("JOKE violates the 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
