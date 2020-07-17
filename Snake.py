from time import process_time
import msvcrt


class Main(object):
    def __init__(self):
        self.grid = []
        for i in range(10):
            self.grid.append([])
            for j in range(10):
                self.grid[i].append(0)

        self.grid[4][5] = 1

        self.direction = "w"

        old_time = process_time()
        while True:

            if msvcrt.kbhit():
                if msvcrt.getch()[0] == 119:
                    self.direction = "w"
                if msvcrt.getch()[0] == 115:
                    self.direction = "s"
                if msvcrt.getch()[0] == 97:
                    self.direction = "a"
                if msvcrt.getch()[0] == 100:
                    self.direction = "d"

            if process_time() - old_time >= 1:
                old_time = process_time()
                self.tick()

    def tick(self):
        for i in range(10):
            print(self.grid[i])
        print(self.direction)


if __name__ == "__main__":
    Main()
