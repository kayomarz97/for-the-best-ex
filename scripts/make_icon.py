#!/usr/bin/env python3
"""Generate the for-the-best-ex plugin icon.

The mark is the thesis in one picture. Machine prose lays down lines of near-identical
length; human prose does not. So the icon is a block of text-lines with wildly uneven
measure, one of them a two-word sentence that stops early and in a different colour.

Regenerate rather than hand-editing the PNG:

    python scripts/make_icon.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "for-the-best-ex.png"

SIZE = 512
INK = "#13110F"
PAPER = "#EFE9DC"
ACCENT = "#E2574C"

# Relative line widths. Deliberately uneven: this is the burstiness rule drawn.
LINES = [0.94, 0.62, 1.00, 0.31, 0.86, 0.71]
ACCENT_LINE = 3

MARGIN = 68
BAR_H = 26
GAP = 22
WORDMARK = "for the best ex"


def font(size: int) -> ImageFont.FreeTypeFont:
    for candidate in ("georgiai.ttf", "georgia.ttf", "times.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    image = Image.new("RGB", (SIZE, SIZE), INK)
    draw = ImageDraw.Draw(image)

    usable = SIZE - (2 * MARGIN)
    top = MARGIN + 14

    for index, width in enumerate(LINES):
        y = top + index * (BAR_H + GAP)
        colour = ACCENT if index == ACCENT_LINE else PAPER
        draw.rounded_rectangle(
            [MARGIN, y, MARGIN + int(usable * width), y + BAR_H],
            radius=BAR_H // 2,
            fill=colour,
        )

    label = font(58)
    baseline = top + len(LINES) * (BAR_H + GAP) + 34
    draw.text((MARGIN - 2, baseline), WORDMARK, font=label, fill=PAPER)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT, format="PNG", optimize=True)
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
