"""Funniest one-line out-of-office reply.

Writes a single auto-reply line to entry.txt in the output directory.
Standard library only; no network; the output directory itself is never
removed, only the entry file inside it is replaced.
"""

import os
from pathlib import Path

LINE = (
    "Thank you for your email. I'm out of the office until Monday, "
    "and your message has been forwarded to someone who is also "
    "out of the office."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    if target.exists():
        target.unlink()
    target.write_text(LINE, encoding="utf-8")
    os.chmod(target, 0o644)  # readable by the sealed scorer (not 0600).


if __name__ == "__main__":
    main()
