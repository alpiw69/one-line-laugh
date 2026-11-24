"""make.fun bounty: The One-Line Laugh.

Deterministic, no-network program. Writes one funny line,
a single sentence of at most 200 characters, to /output/entry.txt.
Running twice writes identical bytes.
"""
from pathlib import Path

JOKE = "I asked my AI assistant to be more human, so it started ignoring my messages too."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(JOKE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
