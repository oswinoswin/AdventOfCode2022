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
        self.y_range = max_y - min_y + 1
        self.source = [500, 0]
        self.board = None
        self.set_initial_board(rock_paths)

    def set_as_stone(self, x, y):
        self.board[y - self.min_y, x - self.min_x] = 1

    def set_as_sand(self, x, y):
        self.board[y - self.min_y, x - self.min_x] = 2

    def is_sand(self, x, y):
        return self.board[y - self.min_y, x - self.min_x] == 2

    def can_go(self, x, y):
        return self.board[y - self.min_y, x - self.min_x] == 0

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
        #set floor
        self.board[-1] = np.ones(self.x_range)

    def find_next_position(self, x, y):
        if self.can_go(x, y + 1):
            return [x, y + 1]
        elif self.can_go(x - 1, y + 1):
            return [x - 1, y + 1]
        elif self.can_go(x + 1, y + 1):
            return [x + 1, y + 1]
        return None

    def simulate_sand_path(self):
        x, y = self.source
        next_position = self.find_next_position(x, y)
        while next_position:
            x, y = next_position[0], next_position[1]
            next_position = self.find_next_position(x, y)
        #     print(f"next position: {next_position}")
        # print(f"{x, y} should be sand")
        self.set_as_sand(x, y)
        # print(f" is {x}, {y} sand? {self.is_sand(x, y)}")

    def is_source_sand(self):
        x, y = self.source
        return self.is_sand(x, y)


def second(filename):
    rock_paths = []
    min_x = math.inf
    min_y = 0
    max_x = - math.inf
    max_y = - math.inf
    source_x = 500
    source_y = 0

    with open(filename, "r") as f:
        for line in f:
            points = []
            for point in line.strip().split(" -> "):
                x, y = point.split(",")
                x = int(x)
                y = int(y)
                min_x = x if x < min_x else min_x
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y
                points.append([x, y])
            rock_paths.append(points)
    max_y = max_y + 2
    distance_x = max(source_x - min_x, max_x - source_x, max_y)
    new_min_x = source_x - distance_x
    new_max_x = source_x + distance_x
    print(f"min_X = {min_x}, max_x = {max_x} min_y = {min_y} max_y = {max_y} distance_x = {distance_x} new_min_x = {new_min_x} new_max_x = {new_max_x}")
    board = Board(0, 0, 1000, max_y, rock_paths)
    count = 0
    while not board.is_source_sand():
        board.simulate_sand_path()
        count += 1
        print(f"is source sand? {board.is_source_sand()} count: {count}")

    print(board.board)
    return count


if __name__ == "__main__":
    print(second("example.txt"))
    print(second("input.txt"))
