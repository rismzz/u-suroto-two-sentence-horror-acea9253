#!/usr/bin/env python3
"""Two-Sentence Horror — writes the story to /output/entry.txt.

The story is embedded as a literal: deterministic, no randomness,
no network. It must be exactly two sentences.

The horror: a child's smart speaker whispers her name at 3 a.m. in
a dead grandmother's voice. Sentence one sets the impossible event;
sentence two closes the escape hatch — nobody taught the device her
name, and the grandmother died before the child was born. Dread
built from two facts that cannot both be true.
"""

import os

LINE = (
    "My daughter's smart speaker whispered her name at 3 a.m. in my "
    "dead mother's voice. We never taught it her name — and my mother "
    "died before she was born."
)


def main() -> None:
    # No trailing newline; exactly two sentences, verified below.
    assert LINE.strip(), "story must not be only whitespace"
    assert "\n" not in LINE, "story must be two sentences on one line"
    assert LINE.replace("a.m.", "am").count(".") == 2, "story must be exactly two sentences"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
