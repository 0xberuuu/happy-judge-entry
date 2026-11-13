"""Entry program: write the prepared image to the output directory.

The image lives in this repository as entry.png. This program copies it,
byte for byte, to $MAKEFUN_OUTPUT_DIR/entry.png (default /output), so
every run produces identical output.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print(f"missing source image: {source}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    # Self-check: the copy must be complete, or the run is a failure.
    if os.path.getsize(target) != os.path.getsize(source):
        print("copied image size does not match source", file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
