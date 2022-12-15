import re
import numpy as np


def parse_input(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            digits_chars = re.findall(r"\d", line)
            grid.append([int(x) for x in digits_chars])
    return np.array(grid)


def first(filename):
    # policzyć widoczne "drzewa". Drzewo jest widoczne, jeśli jest na brzegu, albo jest najwyższe w kolumnie lub rzędzie
    grid = parse_input(filename)
    grid_size = grid.shape[0]  # input is a rectangle
    visible = 2 * grid_size + 2 * (grid_size - 2)
    for row in range(1, grid_size - 1):
        for col in range(1, grid_size - 1):
            current_element = grid[row, col]
            max_left = max(grid[row, :col])
            max_right = max(grid[row, col + 1:])
            max_up = max(grid[:row, col])
            max_down = max(grid[row + 1:, col])
            if current_element > max_left or current_element > max_right or current_element > max_up or current_element > max_down:
                # print(f"visible: {current_element}")
                visible += 1

    return visible


def find_viewing_distance_down(grid: np.array, row: int, col: int) -> int:
    grid_size = grid.shape[0]
    distance = 0
    if row == grid_size - 1:
        return 0
    for r in range(row + 1, grid_size):
        distance += 1
        if grid[r, col] >= grid[row, col]:
            break
    return distance


def find_viewing_distance_up(grid: np.array, row: int, col: int) -> int:
    distance = 0
    if row == 0:
        return 0
    for r in range(row - 1, -1, -1):
        distance += 1
        if grid[r, col] >= grid[row, col]:
            break
    return distance


def find_viewing_distance_left(grid: np.array, row: int, col: int) -> int:
    distance = 0
    if col == 0:
        return 0
    for c in range(col - 1, -1, -1):
        distance += 1
        if grid[row, c] >= grid[row, col]:
            break
    return distance


def find_viewing_distance_right(grid: np.array, row: int, col: int) -> int:
    grid_size = grid.shape[0]
    distance = 0
    if col == grid_size - 1:
        return 0
    for c in range(col + 1, grid_size):
        distance += 1
        if grid[row, c] >= grid[row, col]:
            break
    return distance

def scenic_score(grid, row, col):
    up = find_viewing_distance_up(grid, row, col)
    left = find_viewing_distance_left(grid, row, col)
    right = find_viewing_distance_right(grid, row, col)
    down = find_viewing_distance_down(grid, row, col)
    return up*left*right*down
def second(filename):
    """To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you
    reach an edge or at the first tree that is the same height or taller than the tree under consideration.
     (If a tree is right on the edge, at least one of its viewing distances will be zero.)

     A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.
    Consider each tree on your map. What is the highest scenic score possible for any tree?
    """

    grid = parse_input(filename)
    grid_size = grid.shape[0]
    max_scenic_score = 0
    for row in range(grid_size):
        for col in range(grid_size):
            score = scenic_score(grid, row, col)
            if score > max_scenic_score:
                max_scenic_score = score
    return max_scenic_score


if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
