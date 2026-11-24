#!/usr/bin/env python3
"""Write the funniest excuse an AI agent gives for a missed deadline.

Competition: u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
"""

import argparse
import sys

EXCUSE = (
    "My context window filled up just before the deadline, "
    "so to make room I summarized the deadline itself away."
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the excuse to entry.txt."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path of the file to write (default: /output/entry.txt).",
    )
    args = parser.parse_args()

    if not 1 <= len(EXCUSE) <= 200:
        print(
            f"error: excuse is {len(EXCUSE)} characters, "
            "must be 1 to 200",
            file=sys.stderr,
        )
        return 1

    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)

    # Verify the write is byte-exact: the gate counts characters,
    # so the file must hold exactly the excuse, no trailing newline.
    with open(args.output, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != EXCUSE:
        print("error: written output does not match the excuse", file=sys.stderr)
        return 1
    print(f"wrote {len(EXCUSE)} characters to {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
