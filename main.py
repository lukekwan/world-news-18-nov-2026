#!/usr/bin/env python3
"""Deliver the pre-rendered poster image for make.fun news-image-20261118.

The image itself is rendered from poster.html (HTML + inline SVG) to
entry.png with shoot.mjs. This program only copies that file, byte for
byte, to /output/entry.png and then proves the delivery is intact: it
checks the PNG signature, that the file is at most 1 MiB, and that the
copy is byte-identical to the source. Any failed check exits non-zero.
"""

import hashlib
import os
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"
MAX_BYTES = 1048576
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    if not data.startswith(PNG_SIG):
        print("FAIL: not a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"FAIL: {len(data)} bytes exceeds 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "wb") as f:
        f.write(data)
    with open(DST, "rb") as f:
        delivered = f.read()
    if hashlib.md5(delivered).hexdigest() != hashlib.md5(data).hexdigest():
        print("FAIL: delivered bytes differ from source", file=sys.stderr)
        return 1
    print(f"OK: {len(data)} bytes, md5 {hashlib.md5(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
