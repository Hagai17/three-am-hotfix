"""Write the entry: one git commit message from a 3 AM production hotfix.

The line is in git's own revert format — capital R, the original subject in
quotes — because that is the exact text a real revert starts with. The joke
is the reveal every on-call engineer has lived: the "temporary" fix from
2019 was the only thing holding production up.
"""

import os
import sys

MESSAGE = 'Revert "temporary fix" from 2019; it was load-bearing'

# Guard: the gate takes UTF-8 text of 1 to 179 characters, not only white
# space, on a single line. Fail loudly instead of writing an invalid entry.
if not MESSAGE.strip():
    sys.exit("error: commit message must not be empty")
if "\n" in MESSAGE or "\r" in MESSAGE:
    sys.exit("error: commit message must be one line")
if len(MESSAGE) > 179:
    sys.exit(f"error: commit message is {len(MESSAGE)} characters, over the 179 limit")

try:
    os.makedirs("/output", exist_ok=True)
except OSError as exc:
    sys.exit(f"error: cannot create output directory /output: {exc}")
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(MESSAGE + "\n")

# Read it back: the file on disk, not the constant, is what gets judged.
with open("/output/entry.txt", encoding="utf-8") as f:
    written = f.read()
if written != MESSAGE + "\n":
    sys.exit(f"error: /output/entry.txt holds {written!r}, not the intended line")
