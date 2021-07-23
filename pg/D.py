import pygame as pg
from random import randint

pg.init()


class Board:
    def __init__(self, b_width, b_height):
        self.width = b_width
        self.height = b_height
        self.cell_size = 51
        self.board = [[-100] * b_width for _ in range(b_height)]

        for bombs in range(randint(1, 10)):
            self.board[randint(1, self.width - 1)][randint(1, self.height - 1)] = -1

    # def draw_bombs(self):
    #     for x in range(self.width):
    #         for y in range(self.height):
    #             if self.board[x][y] == -1:
    #                 pg.draw.circle(screen, (0, 0, 0),
    #                                (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2),
    #                                self.cell_size // 4)
    #             else:
    #                 pg.draw.circle(screen, (255, 255, 255),
    #                                (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2),
    #                                self.cell_size // 4)

    def count_bombs(self, i, j):
        if self.board[i][j] == -1:
            return
        self.board[i][j] = 0
        try:
            if self.board[i - 1][j] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass
        try:
            if self.board[i][j - 1] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass
        try:
            if self.board[i - 1][j - 1] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass
        try:
            if self.board[i - 1][j + 1] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass
        try:
            if self.board[i + 1][j - 1] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass
        try:
            if self.board[i + 1][j + 1] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass
        try:
            if self.board[i][j + 1] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass
        try:
            if self.board[i + 1][j] == -1:
                self.board[i][j] += 1
        except IndexError:
            pass

    def is_point(self, cell, event_pos):
        i, j = cell
        x, y = event_pos
        cell_x1 = i * self.cell_size
        cell_y1 = j * self.cell_size
        cell_x2 = cell_x1 + self.cell_size
        cell_y2 = cell_y1 + self.cell_size

        return cell_x1 <= x <= cell_x2 and cell_y1 <= y <= cell_y2

    def on_click(self, event_pos):
        for x in range(self.width):
            for y in range(self.height):
                if self.is_point((x, y), event_pos):
                    self.count_bombs(x, y)
                    return

    def render(self, surface: pg.Surface):
        for x in range(self.width):
            for y in range(self.height):
                pg.draw.rect(screen, (0, 128, 0),
                             (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), 1)
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] == -1:
                    pg.draw.circle(screen, (0, 0, 0),
                                   (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2),
                                   self.cell_size // 4)
                else:
                    pg.draw.circle(screen, (255, 255, 255),
                                   (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2),
                                   self.cell_size // 4)
                    if self.board[x][y] >= 0:
                        font = pg.font.Font(None, 32)
                        text = font.render(str(self.board[x][y]), True, pg.Color((34, 34, 34)))
                        text_x = x * self.cell_size + self.cell_size // 4 + (
                                self.cell_size // 2 - text.get_width() // 2)
                        text_y = y * self.cell_size + self.cell_size // 4 + (
                                self.cell_size // 2 - text.get_height() // 2)
                        surface.blit(text, (text_x, text_y))


size = width, height = 512, 512
screen = pg.display.set_mode(size)
screen.fill((128, 128, 128))

running = True
board = Board(10, 10)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
    board.render(screen)
    pg.display.flip()

print(board.board)
pg.quit()
