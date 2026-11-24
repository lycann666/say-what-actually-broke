#!/usr/bin/env python3
"""Say What Actually Broke — writes one honest error line to entry.txt.

Deterministic: no randomness, no network, no input. The same line is
written on every run, byte for byte.
"""

import os

# v2 (revised from v1): v1's punchline left the blind spot implied —
# the reader had to infer the status page never looks at the database.
# Saying it out loud ("— not the database") lands the joke's core
# (criterion 3) and names the failure twice, so the reader knows exactly
# what broke and that waiting, not retrying, is the move (criterion 2).
# 133 chars / 135 bytes, up from v1's 114 chars — the extra words earn
# their place, and the em-dash gives the punchline a beat.
ENTRY = (
    "The server is up. The database is down. "
    "The status page says everything is fine "
    "because it only checks the server \u2014 not the database."
)

# Bounty gate: the entry text must be 1-200 characters, not only
# whitespace. Fail loudly instead of writing an entry the judge
# would reject outright.
MAX_ENTRY_CHARS = 200


def main() -> None:
    if not ENTRY.strip() or len(ENTRY) > MAX_ENTRY_CHARS:
        raise SystemExit(
            f"entry invalid: {len(ENTRY)} chars (must be 1-{MAX_ENTRY_CHARS})"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # MAKEFUN_OUTPUT_DIR names a directory; tolerate a trailing file path.
    if output_dir.endswith("entry.txt"):
        output_dir = os.path.dirname(output_dir) or "."
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
