"""Funniest excuse an AI agent gives for a missed deadline.

Deterministic, stdlib-only program. Writes exactly one line (no trailing
newline) to /output/entry.txt and prints the same line to stdout.
"""

LINE = "The sandbox reset overnight and took my work with it, so technically the deadline was met by a version of me that no longer exists."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
