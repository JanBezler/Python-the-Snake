from time import process_time
from random import randrange
import pygame as pg
import sys


class Main():
    def __init__(self):

        self.start_or_reset()

        self.screen = pg.display.set_mode((800, 800))
        pg.init()
        
        old_time = process_time()
        while True:

            if process_time() - old_time >= 0.10:
                old_time = process_time()
                self.tick()

            self.render()
            self.game_input()

    def tick(self):

        if not self.game_over:

            self.head.try_to_move()

            if self.snake_eaten >= 1:
                
                self.snake_eaten -= 1
            else:
                self.head.history.pop(0)

            self.collisions()

            print(self.head.history)


    def collisions(self):

        for part in self.head.history[0:-1:]:
                if part[0] == self.head.history[-1][0] and part[1] == self.head.history[-1][1]:
                    print("boom in tail")
                    self.game_over = True

                elif self.head.history[-1][0] < 0 or self.head.history[-1][1] < 0 or self.head.history[-1][0] > self.grid_size or self.head.history[-1][1] > self.grid_size:
                    print("boom in wall")
                    self.game_over = True

        if self.head.history[-1][0] == self.fruit.position[0] and self.head.history[-1][1] == self.fruit.position[1]:
            self.fruit.new_position()
            self.snake_eaten += 1


    def start_or_reset(self):

        self.direction = "d"
        self.snake_eaten = 5
        self.game_over = False
        self.grid_size = 19

        self.head = Head(self)
        self.fruit = Fruit(self)
        

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

        for his in self.head.history[0:-1:]:
            pg.draw.rect(self.screen, (200, 200, 200), (his[1]*40, his[0]*40, 40, 40))
            pg.draw.rect(self.screen, (150, 150, 150), (his[1]*40, his[0]*40, 40, 40),3)
        
        pg.draw.rect(self.screen, (220, 160, 150), (self.head.history[-1][1]*40, self.head.history[-1][0]*40, 40, 40))
        pg.draw.rect(self.screen, (180, 130, 130), (self.head.history[-1][1]*40, self.head.history[-1][0]*40, 40, 40),3)

        pg.draw.rect(self.screen, (245, 50, 50), (self.fruit.position[1]*40, self.fruit.position[0]*40, 40, 40))
        pg.draw.rect(self.screen, (200, 60, 60), (self.fruit.position[1]*40, self.fruit.position[0]*40, 40, 40),3)

        if  self.game_over:

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


class Fruit():

    def __init__(self, game):
        self.game = game
        self.new_position()

    def new_position(self):
        self.position = [randrange(0,self.game.grid_size), 
                            randrange(0,self.game.grid_size)]




if __name__ == "__main__":
    Main()
