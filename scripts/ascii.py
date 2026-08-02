from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from pathlib import Path
from xml.sax.saxutils import escape

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
TARGET_WIDTH = 160


def load_image():

    img = Image.open(INPUT).convert("RGB")

    w, h = img.size

    side = min(w, h)

    left = (w - side) // 2
    top = (h - side) // 2

    img = img.crop((left, top, left + side, top + side))

    img = img.resize((TARGET_WIDTH, TARGET_WIDTH), Image.LANCZOS)

    return img


def preprocess(color):

    gray = ImageOps.grayscale(color)

    gray = ImageEnhance.Contrast(gray).enhance(1.8)
    gray = ImageEnhance.Sharpness(gray).enhance(2.5)

    edges = gray.filter(ImageFilter.FIND_EDGES)
    edges = ImageEnhance.Contrast(edges).enhance(3)

    gray = Image.blend(gray, edges, 0.35)

    return gray


def block(gray, color, x, y):

    brightness = 0

    r = g = b = 0

    count = 0

    for yy in range(y, min(y + CELL_H, gray.height)):
        for xx in range(x, min(x + CELL_W, gray.width)):

            brightness += gray.getpixel((xx, yy))

            rr, gg, bb = color.getpixel((xx, yy))

            r += rr
            g += gg
            b += bb

            count += 1

    brightness /= count

    rgb = (
        int(r / count),
        int(g / count),
        int(b / count),
    )

    return brightness, rgb


def pixel_to_char(value):

    value = 255 - value

    idx = int(value / 255 * (len(ASCII) - 1))

    return ASCII[idx]


def boost(rgb):

    r, g, b = rgb

    r = min(255, int(r * 1.08))
    g = min(255, int(g * 1.08))
    b = min(255, int(b * 1.25))

    return f"rgb({r},{g},{b})"


def make_rows(gray, color):

    rows = []

    for y in range(0, gray.height, CELL_H):

        row = []

        for x in range(0, gray.width, CELL_W):

            bright, rgb = block(gray, color, x, y)

            row.append(
                (
                    pixel_to_char(bright),
                    boost(rgb),
                )
            )

        rows.append(row)

    return rows

def render_svg(rows):

    cols = len(rows[0])
    total_rows = len(rows)

    width = cols * CELL_W + 40
    height = total_rows * CELL_H + 90

    out = []

    out.append(f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<defs>

<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#0d1117"/>
<stop offset="100%" stop-color="#161b22"/>
</linearGradient>

<filter id="glow">
<feGaussianBlur stdDeviation="1.8" result="blur"/>
<feMerge>
<feMergeNode in="blur"/>
<feMergeNode in="SourceGraphic"/>
</feMerge>
</filter>

</defs>

<rect width="100%" height="100%" fill="url(#bg)"/>

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
font-family="JetBrains Mono,Consolas,monospace"
font-size="11">

root@vlastimir:~/portrait

</text>

<text
x="24"
y="58"
fill="#3fb950"
font-family="JetBrains Mono,Consolas,monospace"
font-size="12">

$ render avatar

</text>
""")

    start_x = 18
    start_y = 82

    delay = 0.0

    for row_index, row in enumerate(rows):

        y = start_y + row_index * CELL_H

        for col_index, (char, color) in enumerate(row):

            if char == " ":
                continue

            x = start_x + col_index * CELL_W

            out.append(f"""
<text
x="{x}"
y="{y}"
font-family="JetBrains Mono,Consolas,monospace"
font-size="{FONT_SIZE}"
fill="{color}"
filter="url(#glow)"
opacity="0">{escape(char)}
<animate
attributeName="opacity"
begin="{delay:.2f}s"
dur="0.08s"
from="0"
to="1"
fill="freeze"/>
</text>
""")

        delay += 0.02

    out.append(f"""
<text
x="24"
y="{height-24}"
fill="#58a6ff"
font-family="JetBrains Mono,Consolas,monospace"
font-size="11">

status: ONLINE

<animate
attributeName="opacity"
values="1;0.2;1"
dur="2s"
repeatCount="indefinite"/>

</text>

</svg>
""")

    return "".join(out)


def save(svg):

    OUTPUT.write_text(svg, encoding="utf-8")

    print("Saved:", OUTPUT)

def main():

    if not INPUT.exists():
        print(f"ERROR: {INPUT} not found.")
        return

    print("Loading avatar...")
    color = load_image()

    print("Preprocessing...")
    gray = preprocess(color)

    print("Converting to ASCII...")
    rows = make_rows(gray, color)

    print("Rendering SVG...")
    svg = render_svg(rows)

    print("Saving...")
    save(svg)

    print()
    print("=" * 40)
    print("ASCII portrait generated successfully!")
    print(f"Output: {OUTPUT}")
    print("=" * 40)


if __name__ == "__main__":
    main()
