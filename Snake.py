from time import process_time
import pygame as pg
import sys


class Main():
    def __init__(self):
        self.grid = []
        for i in range(10):
            self.grid.append([])
            for j in range(10):
                self.grid[i].append(0)

        self.grid[4][5] = 1
        self.direction = "w"
        self.old_direction = "w"
        old_time = process_time()

        self.screen = pg.display.set_mode((800, 800))
        pg.init()

        self.head = Head(self)

        while True:

            if process_time() - old_time >= 0.25:
                old_time = process_time()
                self.tick()

            self.render()
            self.game_input()

    def tick(self):
        if self.direction == "w":
            self.head.make_move("w")
        elif self.direction == "s":
            self.head.make_move("s")
        elif self.direction == "a":
            self.head.make_move("a")
        elif self.direction == "d":
            self.head.make_move("d")

        self.old_direction = self.direction

        print(self.head.history[-1])

    def game_input(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                self.direction = "w"
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                self.direction = "s"
            if event.type == pg.KEYDOWN and event.key == pg.K_a:
                self.direction = "a"
            if event.type == pg.KEYDOWN and event.key == pg.K_d:
                self.direction = "d"

    def render(self):

        self.screen.fill((20, 20, 20))
        pg.draw.rect(self.screen, (200, 200, 200),
                     (self.head.history[-1][1]*40, self.head.history[-1][0]*40, 40, 40))
        pg.display.flip()


class Body_part():

    def __init__(self, game, head):
        sefl.game = game
        self.head = head


class Head():

    def __init__(self, game):
        self.history = []
        self.init_position()

    def init_position(self):
        self.position = (5, 5, "w")
        self.history.append(self.position)

    def add_move_to_history(self, move):
        self.history.append(move)

    def make_move(self, direction):
        if direction == "w":
            next_move = (self.history[-1][0]-1, self.history[-1][1], direction)
        elif direction == "s":
            next_move = (self.history[-1][0]+1, self.history[-1][1], direction)
        elif direction == "a":
            next_move = (self.history[-1][0], self.history[-1][1]-1, direction)
        elif direction == "d":
            next_move = (self.history[-1][0], self.history[-1][1]+1, direction)

        self.add_move_to_history(next_move)


if __name__ == "__main__":
    Main()
