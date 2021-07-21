from math import sqrt, atan2, cos, sin
from random import randint, randrange
from PIL import Image
from PIL import ImageDraw

width = 500
height = 500

image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)
used_coords = []

for i in range(randint(1, 10)):
    x, y = randrange(0, width, 50), randrange(0, height, 50)
    if (x + 25, y + 25) in used_coords:
        continue
    draw.ellipse((x + 20, y + 20, x + 30, y + 30), outline='yellow', fill='yellow')
    used_coords.append((x + 25, y + 25))

for i in range(10):
    for j in range(10):
        x = int(width/10 * i) + 25
        y = int(height/10 * j) + 25
        if (x, y) in used_coords:
            continue
        minimal_distance = 10000
        minimal_coords = (10000, 10000)
        for k in range(len(used_coords)):
            if sqrt((used_coords[k][0] - x)**2 + (used_coords[k][1] - y)**2) < minimal_distance:
                minimal_distance = sqrt((used_coords[k][0] - x)**2 + (used_coords[k][1] - y)**2)
                minimal_coords = (used_coords[k][0], used_coords[k][1])
        angle = atan2(minimal_coords[1] - y, minimal_coords[0] - x)
        draw.line((x, y, x + 25 * cos(angle), y + 25 * sin(angle)),
                  fill='white', width=2)
        draw.ellipse((x + 25 * cos(angle) - 2, y + 25 * sin(angle) - 2,
                      x + 25 * cos(angle) + 2, y + 25 * sin(angle) + 2),
                     fill='red')

image.save("vectors.png", "PNG")
