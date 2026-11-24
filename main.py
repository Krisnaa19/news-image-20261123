#!/usr/bin/env python3
"""Entry program for the 23 November 2026 world-news image.

Copies the bundled entry.png (1024x1024, under 1 MiB) to
/output/entry.png. No network, no randomness: two runs write
the same bytes.

After the copy the program reads both files back and compares
their size and SHA-256 digest, so a truncated or corrupted write
is caught here with a clear error instead of silently shipping a
broken image.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    src = os.path.join(HERE, "entry.png")
    dst = "/output/entry.png"
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, dst)
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        raise SystemExit(
            "copy failed: %s is %d bytes but %s is %d bytes"
            % (src, src_size, dst, dst_size)
        )
    src_hash = _sha256(src)
    dst_hash = _sha256(dst)
    if src_hash != dst_hash:
        raise SystemExit(
            "copy failed: %s sha256 %s != %s sha256 %s"
            % (src, src_hash, dst, dst_hash)
        )
    print("wrote %s (%d bytes, sha256 %s)" % (dst, dst_size, dst_hash))


if __name__ == "__main__":
    main()
