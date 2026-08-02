from PIL import Image
import os
from xml.sax.saxutils import escape

INPUT = "assets/avatar.png"
OUTPUT = "assets/portrait.svg"

ASCII = "@%#*+=-:. "

WIDTH = 90
FONT_SIZE = 8
LINE_HEIGHT = 8
FONT = "Consolas"


def image_to_ascii(path):
    img = Image.open(path).convert("L")

    aspect = img.height / img.width
    height = int(WIDTH * aspect * 0.55)

    img = img.resize((WIDTH, height))

    pixels = img.load()

    lines = []

    for y in range(height):
        row = ""
        for x in range(WIDTH):
            value = pixels[x, y]
            index = int(value / 255 * (len(ASCII) - 1))
            row += ASCII[index]
        lines.append(row)

    return lines


def make_svg(lines):
    width = WIDTH * FONT_SIZE * 0.62
    height = len(lines) * LINE_HEIGHT + 20

    svg = []

    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
    )

    svg.append(
        '<rect width="100%" height="100%" fill="#0d1117"/>'
    )

    svg.append(
        f'<text x="10" y="18" '
        f'font-family="{FONT}" '
        f'font-size="{FONT_SIZE}" '
        f'fill="#7aa2ff" '
        f'xml:space="preserve">'
    )

    y = 18

    for line in lines:
        svg.append(
            f'<tspan x="10" y="{y}">{escape(line)}</tspan>'
        )
        y += LINE_HEIGHT

    svg.append("</text>")
    svg.append("</svg>")

    return "\n".join(svg)


def main():
    if not os.path.exists(INPUT):
        print(f"Cannot find {INPUT}")
        return

    lines = image_to_ascii(INPUT)

    svg = make_svg(lines)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
