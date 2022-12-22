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
        self.y_range = max_y - min_y + 2 # ONE MORE ROW FOR THE SAN
        self.source = [500, 0]
        self.board = None
        self.set_initial_board(rock_paths)

    def set_as_stone(self, x, y):
        self.board[y - self.min_y + 1, x - self.min_x] = 1

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


def first(filename):
    rock_paths = []
    min_x = math.inf
    min_y = math.inf
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
                min_y = y if y < min_y else min_y
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y
                points.append([x, y])
            rock_paths.append(points)

    board = Board(min_x, min_y, max_x, max_y, rock_paths)
    np.set_printoptions(threshold=sys.maxsize)
    print(board.board)
    return rock_paths


def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))
