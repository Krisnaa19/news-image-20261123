#!/usr/bin/env python3
"""Entry program for the 23 November 2026 world-news image.

Copies the bundled entry.png (1024x1024, under 1 MiB) to
/output/entry.png. No network, no randomness: two runs write
the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")
    print("wrote /output/entry.png")


if __name__ == "__main__":
    main()
