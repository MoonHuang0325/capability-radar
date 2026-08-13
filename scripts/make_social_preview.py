#!/usr/bin/env python3
"""Generate .github/social-preview.png (1280x640) for capability-radar."""
from PIL import Image, ImageDraw, ImageFont
import matplotlib
from pathlib import Path

_FONT_DIR = Path(matplotlib.get_data_path()) / "fonts" / "ttf"

W, H = 1280, 640
BG = (13, 17, 23)          # GitHub dark canvas
RING = (48, 54, 61)        # subtle radar rings
ACCENT = (63, 185, 80)     # GitHub green
AMBER = (210, 153, 34)     # attention amber
TEXT = (230, 237, 243)
MUTED = (125, 133, 144)

def font(size, bold=True):
    path = _FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(str(path), size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Radar rings on the right side
cx, cy = 1050, 320
for r in (70, 140, 210, 280):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RING, width=2)
# Sweep line + blips
d.line([cx, cy, cx + 200, cy - 196], fill=(46, 160, 67), width=3)
d.ellipse([cx + 130, cy - 140, cx + 146, cy - 124], fill=ACCENT)
d.ellipse([cx - 100, cy - 90, cx - 88, cy - 78], fill=AMBER)
d.ellipse([cx + 40, cy + 150, cx + 52, cy + 162], fill=ACCENT)
d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=ACCENT)

# Text block
x = 90
d.text((x, 110), "CAPABILITY RADAR", font=font(72), fill=TEXT)
d.text((x, 215), "What companies hire for  ×  What companies pay for",
       font=font(30, bold=False), fill=MUTED)

rows = [
    ("▲", "Agent building & workflow automation", "43.8% of new AI jobs", ACCENT),
    ("▲", "AI evaluation & observability", "largest supply gap", ACCENT),
    ("▲", "LLM security procurement", "now in central catalogs", AMBER),
]
y = 300
for arrow, label, stat, color in rows:
    d.text((x, y), arrow, font=font(26), fill=color)
    d.text((x + 44, y + 2), label, font=font(26, bold=False), fill=TEXT)
    lw = d.textlength(label, font=font(26, bold=False))
    d.text((x + 60 + lw, y + 6), "· " + stat, font=font(22, bold=False), fill=MUTED)
    y += 62

d.text((x, 545), "Open Source  ·  Updated Weekly  ·  Evidence-graded A/B/C",
       font=font(22, bold=False), fill=MUTED)

img.save(".github/social-preview.png")
print("saved .github/social-preview.png", img.size)
