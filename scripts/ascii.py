from pathlib import Path
from urllib.request import urlretrieve
from PIL import Image

# ----------------------------
# Configuration
# ----------------------------

USERNAME = "Vlastimir0500"

WIDTH = 80

ASCII = "@%#*+=-:. "

ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)

AVATAR = ASSETS / "avatar.png"
OUTPUT = ASSETS / "portrait.svg"

# ----------------------------
# Download avatar
# ----------------------------

def download_avatar():
    url = f"https://github.com/{USERNAME}.png"
    print("Downloading avatar...")
    urlretrieve(url, AVATAR)
    print("Done.")

# ----------------------------
# Resize
# ----------------------------

def resize(image):

    width, height = image.size

    aspect = height / width

    new_height = int(WIDTH * aspect * 0.55)

    return image.resize((WIDTH, new_height))

# ----------------------------
# Convert to grayscale
# ----------------------------

def grayscale(image):
    return image.convert("L")

# ----------------------------
# Pixels -> ASCII
# ----------------------------

def to_ascii(image):

    pixels = image.getdata()

    chars = ""

    for pixel in pixels:
        chars += ASCII[pixel * (len(ASCII)-1) // 255]

    return chars

# ----------------------------
# SVG
# ----------------------------

def save_svg(chars, width, height):

    font_size = 10

    spacing = 9

    svg = []

    svg.append(
f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width*spacing}"
height="{height*spacing}"
viewBox="0 0 {width*spacing} {height*spacing}">

<rect width="100%" height="100%" fill="#0d1117"/>

<style>

text {{
font-family: monospace;
font-size: {font_size}px;
fill: #58a6ff;
}}

</style>
''')

    index = 0

    delay = 0

    for y in range(height):

        for x in range(width):

            c = chars[index]

            svg.append(f'''
<text
x="{x*spacing}"
y="{(y+1)*spacing}"
opacity="0">

{c}

<animate
attributeName="opacity"
begin="{delay:.2f}s"
dur="0.2s"
fill="freeze"
from="0"
to="1"/>

</text>
''')

            index += 1

        delay += 0.03

    svg.append("</svg>")

    OUTPUT.write_text("\n".join(svg), encoding="utf8")

    print("Saved:", OUTPUT)

# ----------------------------
# Main
# ----------------------------

def main():

    download_avatar()

    img = Image.open(AVATAR)

    img = resize(img)

    img = grayscale(img)

    width, height = img.size

    chars = to_ascii(img)

    save_svg(chars, width, height)

if __name__ == "__main__":
    main()
