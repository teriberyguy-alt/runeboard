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
# FONT (slightly smaller fits circles better)
# ===============================
font = ImageFont.truetype("font.ttf", 28)

# ===============================
# GRID CONFIG (TUNED TO YOUR IMAGE)
# ===============================
rows = 3
cols = 11

start_x = 42
start_y = 78   # moved down into yellow circle area

cell_width = 74
cell_height = 138

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

    cell_x = start_x + col * cell_width
    cell_y = start_y + row * cell_height

    # Measure text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center in circle zone
    x = cell_x - text_width // 2 + 35
    y = cell_y - text_height // 2

    # Shadow
    draw.text((x + 2, y + 2), text, font=font, fill="black")

    # Gold text
    draw.text((x, y), text, font=font, fill=(212, 175, 55))

# ===============================
# SAVE
# ===============================
image.save("output.png")
print("Image generated successfully!")
