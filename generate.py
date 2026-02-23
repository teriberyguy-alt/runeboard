from PIL import Image, ImageDraw, ImageFont
import json

# Load image
image = Image.open("base.png").convert("RGBA")
draw = ImageDraw.Draw(image)

# Load rune counts
with open("counts.json", "r") as f:
    counts = json.load(f)

# Load font
font = ImageFont.truetype("font.ttf", 28)

# TODO: Adjust coordinates to match your image
rune_positions = {
    "El": (110, 95),
    "Eld": (180, 95),
    "Tir": (250, 95),
    "Nef": (320, 95),
    "Eth": (390, 95),
    "Ith": (460, 95),
    "Tal": (530, 95),
    "Ral": (600, 95),
    "Ort": (670, 95),
}

for rune, position in rune_positions.items():
    count = counts.get(rune, 0)

    # Shadow
    draw.text((position[0]+2, position[1]+2), str(count),
              font=font, fill="black")

    # Main text
    draw.text(position, str(count),
              font=font, fill=(212,175,55))

image.save("output.png")
