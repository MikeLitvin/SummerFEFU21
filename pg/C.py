import pygame as pg

size = width, height = 300, 300
screen = pg.display.set_mode(size)
screen2 = pg.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0

drawing = False
running = True
rectangles = []
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            drawing = True
            x1, y1 = event.pos
        if event.type == pg.MOUSEBUTTONUP:
            rectangles.append([(x1, y1), (w, h)])
            screen2.blit(screen, (0, 0))
            drawing = False
        if event.type == pg.MOUSEMOTION:
            w, h = event.pos[0] - x1, event.pos[1] - y1
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z and pg.key.get_mods() & pg.KMOD_LCTRL:
                if len(rectangles) > 0:
                    rectangles.pop()
                screen2.fill((0, 0, 0))
                for element in rectangles:
                    pg.draw.rect(screen2, (128, 128, 128), (element[0], element[1]), 5)

    screen.fill(pg.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:
        pg.draw.rect(screen, (128, 128, 128), ((x1, y1), (w, h)), 5)
    pg.display.flip()

pg.quit()

