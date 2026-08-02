from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from pathlib import Path
import math
import os

ROOT = Path(__file__).resolve().parents[1]

INPUT = ROOT / "assets" / "avatar.png"
OUTPUT = ROOT / "assets" / "portrait.svg"

ASCII = (
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUXYzcvunxrjft/"
    "\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
)

FONT_SIZE = 7
CELL_W = 5
CELL_H = 9
WIDTH = 150


def fit_image(img):
    w, h = img.size

    target = 1.0

    if w > h:
        nw = h
        left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    else:
        nh = w
        top = (h - nh) // 2
        img = img.crop((0, top, w, top + nh))

    img = img.resize((WIDTH, WIDTH), Image.LANCZOS)

    return img


def preprocess(img):

    gray = ImageOps.grayscale(img)

    gray = ImageEnhance.Contrast(gray).enhance(1.6)
    gray = ImageEnhance.Sharpness(gray).enhance(2.2)

    edges = gray.filter(ImageFilter.FIND_EDGES)

    edges = ImageEnhance.Contrast(edges).enhance(3)

    merged = Image.blend(gray, edges, 0.35)

    return merged


def block_average(img, rgb, x, y):

    total = 0

    r = g = b = 0

    count = 0

    for yy in range(y, min(y + CELL_H, img.height)):
        for xx in range(x, min(x + CELL_W, img.width)):

            total += img.getpixel((xx, yy))

            rr, gg, bb = rgb.getpixel((xx, yy))

            r += rr
            g += gg
            b += bb

            count += 1

    return (
        total / count,
        (
            int(r / count),
            int(g / count),
            int(b / count),
        ),
    )


def brightness_to_char(value):

    value = 255 - value

    idx = int(value / 255 * (len(ASCII) - 1))

    return ASCII[idx]


def colorize(rgb):

    r, g, b = rgb

    r = min(255, int(r * 1.12))
    g = min(255, int(g * 1.12))
    b = min(255, int(b * 1.30))

    return f"rgb({r},{g},{b})"


def build_ascii(gray, color):

    rows = []

    for y in range(0, gray.height, CELL_H):

        line = []

        for x in range(0, gray.width, CELL_W):

            bright, rgb = block_average(gray, color, x, y)

            ch = brightness_to_char(bright)

            line.append((ch, colorize(rgb)))

        rows.append(line)

    return rows
    from xml.sax.saxutils import escape


def build_svg(rows):

    cols = len(rows[0])
    lines = len(rows)

    width = cols * CELL_W + 40
    height = lines * CELL_H + 90

    svg = []

    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<defs>

<linearGradient id="bg"
x1="0%" y1="0%"
x2="100%" y2="100%">

<stop offset="0%" stop-color="#0d1117"/>
<stop offset="100%" stop-color="#161b22"/>

</linearGradient>

<filter id="glow">

<feGaussianBlur stdDeviation="2.2" result="blur"/>

<feMerge>
<feMergeNode in="blur"/>
<feMergeNode in="SourceGraphic"/>
</feMerge>

</filter>

</defs>

<rect
width="100%"
height="100%"
fill="url(#bg)"/>

<rect
x="8"
y="8"
width="{width-16}"
height="{height-16}"
rx="12"
fill="#010409"
stroke="#30363d"/>

<circle cx="28" cy="25" r="5" fill="#ff5f56"/>
<circle cx="46" cy="25" r="5" fill="#ffbd2e"/>
<circle cx="64" cy="25" r="5" fill="#27c93f"/>

<text
x="90"
y="30"
fill="#8b949e"
font-size="11"
font-family="JetBrains Mono,Consolas,monospace">

root@vlastimir:~/portrait

</text>

<text
x="24"
y="58"
fill="#3fb950"
font-size="12"
font-family="JetBrains Mono,Consolas,monospace">

$ render avatar

</text>

''')

    delay = 0.0

    start_y = 80

    for row_index, row in enumerate(rows):

        y = start_y + row_index * CELL_H

        for col_index, (char, color) in enumerate(row):

            if char == " ":
                continue

            x = 18 + col_index * CELL_W

            svg.append(f'''
<text
x="{x}"
y="{y}"
font-family="JetBrains Mono,Consolas,monospace"
font-size="{FONT_SIZE}"
fill="{color}"
filter="url(#glow)"
opacity="0">

{escape(char)}

<animate
attributeName="opacity"
begin="{delay:.2f}s"
dur="0.12s"
fill="freeze"
from="0"
to="1"/>

</text>
''')

        delay += 0.025

    svg.append(f'''

<text
x="24"
y="{height-22}"
fill="#58a6ff"
font-size="11"
font-family="JetBrains Mono,Consolas,monospace">

status: ONLINE

<animate
attributeName="opacity"
values="1;0.2;1"
dur="2s"
repeatCount="indefinite"/>

</text>

</svg>
''')

    return "\n".join(svg)


def save_svg(svg):

    OUTPUT.write_text(svg, encoding="utf-8")

    print(f"Saved → {OUTPUT}")
    def main():

    if not INPUT.exists():
        print(f"Avatar not found: {INPUT}")
        return

    print("Loading avatar...")

    color = Image.open(INPUT).convert("RGB")

    color = fit_image(color)

    gray = preprocess(color)

    print("Generating ASCII...")

    rows = build_ascii(gray, color)

    print("Rendering SVG...")

    svg = build_svg(rows)

    save_svg(svg)

    print()
    print("====================================")
    print(" ASCII portrait generated!")
    print(f" Saved to: {OUTPUT}")
    print("====================================")


if __name__ == "__main__":
    main()
