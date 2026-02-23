from PIL import Image, ImageDraw, ImageFont
import json

# Load base image
image = Image.open("base.png").convert("RGBA")
draw = ImageDraw.Draw(image)

# Load rune counts
with open("counts.json", "r") as f:
    counts = json.load(f)

font = ImageFont.truetype("font.ttf", 32)

# Grid settings (adjust if needed)
rows = 3
cols = 11

start_x = 40
start_y = 40
x_spacing = 110
y_spacing = 120

# Rune order (left to right, top to bottom)
rune_order = [
    "El","Eld","Tir","Nef","Eth","Ith","Tal","Ral","Ort","Thul","Amn",
    "Sol","Shael","Dol","Hel","Io","Lum","Ko","Fal","Lem","Pul","Um",
    "Mal","Ist","Gul","Vex","Ohm","Lo","Sur","Ber","Jah","Cham","Zod"
]

index = 0

for row in range(rows):
    for col in range(cols):
        if index >= len(rune_order):
            break

        rune = rune_order[index]
        count = counts.get(rune, 0)

        x = start_x + col * x_spacing
        y = start_y + row * y_spacing

        # Shadow
        draw.text((x+2, y+2), str(count), font=font, fill="black")

        # Gold number
        draw.text((x, y), str(count), font=font, fill=(212,175,55))

        index += 1

image.save("output.png")
print("Image generated!")
