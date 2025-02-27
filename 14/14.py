import math
import sys

import numpy as np
class Board:
    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int, rock_paths: list):
        self.min_x = min_x
        self.min_y = min_y
        self.max_y = max_y
        self.max_x = max_x
        self.rock_paths = rock_paths
        self.x_range = max_x - min_x + 1
        self.y_range = max_y - min_y + 2 # ONE MORE ROW FOR THE SAND
        self.source = [500, 0]
        self.board = None
        self.set_initial_board(rock_paths)

    def set_as_stone(self, x, y):
        self.board[y - self.min_y + 1, x - self.min_x] = 1

    def is_stone(self, x, y):
        return self.board[y - self.min_y + 1, x - self.min_x] == 1

    def set_as_sand(self, x, y):
        self.board[y - self.min_y + 1, x - self.min_x] = 2

    def is_sand(self, x, y):
        return self.board[y - self.min_y + 1, x - self.min_x] == 2

    def can_go(self, x, y):
        # if x <= self.min_x or x >= self.max_x or y <= self.min_y or y >= self.max_y:
        #     return False
        return self.board[y - self.min_y + 1, x - self.min_x] == 0

    def get_board_value(self, x, y):
        return self.board[y - self.min_y + 1, x - self.min_x]

    def get_real_index(self, x, y):
        return y - self.min_y + 1,  x - self.min_x

    def draw_line(self, source, destination): #source = x,y
        if source[0] == destination[0]:
            x = source[0]
            y_min = min(source[1], destination[1])
            y_max = max(source[1], destination[1])
            for y in range(y_min, y_max + 1):
                self.set_as_stone(x, y)

        if source[1] == destination[1]:
            y = source[1]
            x_min = min(source[0], destination[0])
            x_max = max(source[0], destination[0])
            for x in range(x_min, x_max + 1):
                self.set_as_stone(x, y)

    def set_initial_board(self, rock_paths):
        self.board = np.zeros([self.y_range, self.x_range])
        for rock_path in rock_paths:
            for i in range(1, len(rock_path)):
                self.draw_line(rock_path[i - 1], rock_path[i])

    def find_next_position(self, x, y):
        try:
            if self.can_go(x, y + 1):
                return [x, y + 1]
            elif self.can_go(x - 1, y + 1):
                return [x - 1, y + 1]
            elif self.can_go(x + 1, y + 1):
                return [x + 1, y + 1]
        except IndexError:
            pass
        return [-1, - 1] # out of range

    def simulate_sand_path(self):
        x, y = self.source
        next_x, next_y = self.find_next_position(x, y)
        while next_x != -1 and next_y != -1:
            x, y = next_x, next_y
            next_x, next_y = self.find_next_position(next_x, next_y)
        return x, y



def first(filename):
    rock_paths = []
    min_x = math.inf
    # min_y = math.inf
    max_x = - math.inf
    max_y = - math.inf

    with open(filename, "r") as f:
        for line in f:
            points = []
            for point in line.strip().split(" -> "):
                x, y = point.split(",")
                x = int(x)
                y = int(y)
                min_x = x if x < min_x else min_x
                # min_y = y if y < min_y else min_y
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y
                points.append([x, y])
            rock_paths.append(points)

    board = Board(min_x, 0, max_x, max_y, rock_paths)
    np.set_printoptions(threshold=sys.maxsize)
    print(board.board)
    print(f"x_min = {board.min_x}, x_max = {board.max_x} y_min = {board.min_y}, x_max = {board.max_y}")
    count = 0
    x = 0
    y = 0
    while True:
        x, y = board.simulate_sand_path()
        if x == -1:
            break
        count += 1
        print(x, y, count)
        board.set_as_sand(x, y)
        print(board.board)

    return count



if __name__ == "__main__":
    print(first("example.txt"))
    # print(first("input.txt"))

