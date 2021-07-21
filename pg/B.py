import pygame as pg
pg.init()
size = width, height = 300, 300
screen = pg.display.set_mode(size)
pg.draw.rect(screen, (128, 128, 128), (0, 0, 30, 30), 0)
pg.display.flip()

running = True
x = 0
y = 0
rect_x = 0
rect_y = 0
drag_mode = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if rect_x <= mouse_pos[0] <= rect_x + 30 and rect_y <= mouse_pos[1] <= rect_y + 30:
                drag_mode = True
        if event.type == pg.MOUSEBUTTONUP:
            drag_mode = False
        if event.type == pg.MOUSEMOTION:
            x, y = event.pos
    if drag_mode:
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (128, 128, 128), (x - 15, y - 15, 30, 30), 0)
        rect_x = x
        rect_y = y
        pg.display.flip()
pg.quit()
