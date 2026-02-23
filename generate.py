from PIL import Image, ImageDraw, ImageFont
import json

# Load base image
image = Image.open("base.png").convert("RGBA")
draw = ImageDraw.Draw(image)

# Load rune counts
with open("counts.json", "r") as f:
    counts = json.load(f)

font = ImageFont.truetype("font.ttf", 32)

# Grid settings
rows = 3
cols = 11

start_x = 40
start_y = 40
x_spacing = 110
y_spacing = 120

# Rune order (fixed mapping)
rune_order = [
    "El","Eld","Tir","Nef","Eth","Ith","Tal","Ral","Ort","Thul","Amn",
    "Sol","Shael","Dol","Hel","Io","Lum","Ko","Fal","Lem","Pul","Um",
    "Mal","Ist","Gul","Vex","Ohm","Lo","Sur","Ber","Jah","Cham","Zod"
]

# Draw counts directly from rune index mapping
for index, rune in enumerate(rune_order):

    row = index // cols
    col = index % cols

    if row >= rows:
        break

    count = counts.get(rune, 0)

    x = start_x + col * x_spacing
    y = start_y + row * y_spacing

    text = str(count)

    # Shadow (for readability)
    draw.text((x + 2, y + 2), text, font=font, fill="black")

    # Gold number
    draw.text((x, y), text, font=font, fill=(212, 175, 55))

image.save("output.png")
print("Image generated!")
