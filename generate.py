from PIL import Image, ImageDraw, ImageFont
import json

# ===============================
# LOAD IMAGE
# ===============================
image = Image.open("base.png").convert("RGBA")
draw = ImageDraw.Draw(image)

# ===============================
# LOAD COUNTS
# ===============================
with open("counts.json", "r") as f:
    counts = json.load(f)

# ===============================
# FONT
# ===============================
font = ImageFont.truetype("font.ttf", 26)

# ===============================
# GRID CONFIG (ACTUAL CALIBRATION)
# ===============================
rows = 3
cols = 11

start_x = 60
start_y = 95      # Correct first row center

x_spacing = 70
y_spacing = 110   # Correct vertical spacing

# ===============================
# RUNE ORDER
# ===============================
rune_order = [
    "El","Eld","Tir","Nef","Eth","Ith","Tal","Ral","Ort","Thul","Amn",
    "Sol","Shael","Dol","Hel","Io","Lum","Ko","Fal","Lem","Pul","Um",
    "Mal","Ist","Gul","Vex","Ohm","Lo","Sur","Ber","Jah","Cham","Zod"
]

# ===============================
# DRAW NUMBERS
# ===============================
for index, rune in enumerate(rune_order):

    row = index // cols
    col = index % cols

    if row >= rows:
        break

    count = counts.get(rune, 0)
    text = str(count)

    center_x = start_x + col * x_spacing
    center_y = start_y + row * y_spacing

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = center_x - text_width // 2
    y = center_y - text_height // 2

    draw.text((x + 2, y + 2), text, font=font, fill="black")
    draw.text((x, y), text, font=font, fill=(212, 175, 55))

image.save("output.png")
print("Image generated successfully!")
