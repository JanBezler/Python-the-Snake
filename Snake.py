from time import process_time
import pygame as pg
import sys


class Main():
    def __init__(self):

        self.direction = "w"
        old_time = process_time()
        self.snake_eaten = 5
        self.game_over = False
        self.grid_size = 19

        self.screen = pg.display.set_mode((800, 800))
        pg.init()

        self.head = Head(self)

        while True:

            if process_time() - old_time >= 0.15:
                old_time = process_time()
                self.tick()

            self.render()
            self.game_input()

    def tick(self):

        if not self.game_over:

            self.head.try_to_move()

            print(self.head.history)

            if self.snake_eaten >= 1:
                
                self.snake_eaten -= 1
            else:
                self.head.history.pop(0)

            for part in self.head.history[0:-1:]:
                if part[0] == self.head.history[-1][0] and part[1] == self.head.history[-1][1]:
                    print("boom in tail")
                    self.game_over = True

                elif self.head.history[-1][0] < 0 or self.head.history[-1][1] < 0 or self.head.history[-1][0] > self.grid_size or self.head.history[-1][1] > self.grid_size:
                    print("boom in wall")
                    self.game_over = True

        
        else:
            pass
            #del(self.head)
            

    def reset(self):
        pass
        

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

        if not self.game_over:
            for his in self.head.history:
                pg.draw.rect(self.screen, (200, 200, 200), (his[1]*40, his[0]*40, 40, 40))
                pg.draw.rect(self.screen, (150, 150, 150), (his[1]*40, his[0]*40, 40, 40),3)

        else:
            myfont = pg.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render("Game over!", True, (200, 160, 220))
            self.screen.blit(textsurface, (0,0))

        pg.display.flip()


class Head():

    def __init__(self, game):
        self.history = []
        self.init_position()
        self.game = game

    def init_position(self):
        self.position = (5, 5, "w")
        self.history.append(self.position)

    def add_move_to_history(self, move):
        self.history.append(move)


    def try_to_move(self):

        if self.game.direction == "w"  and self.history[-1][2] == "s":
            self.make_move("s")
        elif self.game.direction == "w":
            self.make_move("w")

        if self.game.direction == "s" and self.history[-1][2] == "w":
            self.make_move("w")
        elif self.game.direction == "s":
            self.make_move("s")

        if self.game.direction == "a" and self.history[-1][2] == "d":
            self.make_move("d")
        elif self.game.direction == "a":
            self.make_move("a")

        if self.game.direction == "d" and self.history[-1][2] == "a":
            self.make_move("a")
        elif self.game.direction == "d":
            self.make_move("d")

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
