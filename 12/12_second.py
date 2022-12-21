import math


class Node:
    value: int
    neighbours: list
    is_source: bool
    is_destination: bool
    steps_from_start: int
    came_from = None  # should be Node

    def __init__(self, value: str):
        self.value = self.set_value(value)
        self.char_value: str = value
        self.neighbours = []
        self.is_source = (value == "a") or (value == "S")
        self.is_destination = (value == "E")
        self.steps_from_start = 0 if self.is_source else math.inf
        self.came_from = None

    def __str__(self):
        # return str(self.__dict__)
        return f"value: {self.get_char_value()} steps: {self.steps_from_start} neighbours: {[n.get_char_value() for n in self.neighbours]}"

    def can_go_to(self, another_node) -> bool:
        if self.is_destination:
            return False
        return self.value + 1 >= another_node.value

    def get_char_value(self) -> str:
        return self.char_value

    def add_neighbours(self, potential_neighbours):
        for neighbour in potential_neighbours:
            if self.can_go_to(neighbour):
                self.neighbours.append(neighbour)

    def set_value(self, value):
        if value == "S":
            return ord("a")
        if value == "E":
            return ord("z")
        return ord(value)


def bfs(source: Node, destination: Node):
    queue = [source]
    while queue:
        current_node = queue.pop(0)
        # print(f"Inspecting: {current_node}")
        for neighbour in current_node.neighbours:
            if current_node.steps_from_start + 1 < neighbour.steps_from_start:
                neighbour.steps_from_start = current_node.steps_from_start + 1
                neighbour.came_from = current_node
                queue.append(neighbour)
    return destination.steps_from_start


def clear(nodes_grid):
    for row in nodes_grid:
        for node in row:
            node.steps_from_start = 0 if node.is_source else math.inf


def second(filename):
    char_grid = []
    with open(filename, "r") as f:
        for line in f:
            row = [char for char in line.strip()]
            char_grid.append(row)

    nodes_grid = []
    sources = []
    destination_node = None
    for row in range(len(char_grid)):
        nodes_row = []
        for col in range(len(char_grid[row])):
            new_node = Node(char_grid[row][col])
            if char_grid[row][col] == "a" or char_grid[row][col] == "S":
                new_node.is_source = True
                sources.append(new_node)
            if char_grid[row][col] == "E":
                new_node.is_destination = True
                destination_node = new_node
            nodes_row.append(new_node)
        nodes_grid.append(nodes_row)

    # now find neighbours
    for row in range(len(nodes_grid)):
        for col in range(len(nodes_grid[row])):
            potential_neighbours = []
            if row > 0:
                potential_neighbours.append(nodes_grid[row - 1][col])
            if row + 1 < len(nodes_grid):
                potential_neighbours.append(nodes_grid[row + 1][col])
            if col > 0:
                potential_neighbours.append(nodes_grid[row][col - 1])
            if col + 1 < len(nodes_grid[row]):
                potential_neighbours.append(nodes_grid[row][col + 1])

            nodes_grid[row][col].add_neighbours(potential_neighbours)
            # print(nodes_grid[row][col])

    best_distance = math.inf

    for source in sources:
        distance = bfs(source, destination_node)
        if distance < best_distance:
            best_distance = distance
        clear(nodes_grid)

    return best_distance


if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
