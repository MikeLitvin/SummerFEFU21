import pygame as pg
pg.init()
w = int(input())
n = int(input())
size = w, w
screen = pg.display.set_mode(size)
screen.fill((0, 0, 0))

color1, color2, color3 = 255, 255, 255
color = pg.Color(color1, color2, color3)


def color_reverse(color_rev):
    return 255 if color_rev == 0 else 0


for x in range(n):
    for y in range(n):
        pg.draw.rect(screen, color, (x * w / n, y * w / n, w // n, w // n), 0)
        color1 = color2 = color3 = color_reverse(color1)
        color = pg.Color(color1, color2, color3)

pg.display.flip()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()
