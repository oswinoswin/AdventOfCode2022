import math
class Node:
    value: int
    neighbours: list
    is_source: bool
    is_destination: bool
    steps_from_start: int
    came_from = None #should be Node

    def __init__(self, value: str):
        self.value = self.set_value(value)
        self.neighbours = []
        self.is_source = (value == "S")
        self.is_destination = (value == "E")
        self.steps_from_start = 0 if self.is_source else math.inf
        self.came_from = None

    def __str__(self):
        # return str(self.__dict__)
        return f"value: {self.get_char_value()} steps: {self.steps_from_start} neighbours: {[n.get_char_value() for n in self.neighbours]}"

    def can_go_to(self, another_node) -> bool:
        if self.is_source:
            return True
        if self.is_destination:
            return False
        return self.value + 1 >= another_node.value

    def get_char_value(self) -> str:
        if self.is_source:
            return "S"
        if self.is_destination:
            return "E"
        return chr(self.value)

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


# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }
#
# visited = [] # List for visited nodes.
# queue = []     #Initialize a queue
#
# def bfs(visited, graph, node): #function for BFS
#   visited.append(node)
#   queue.append(node)
#
#   while queue:          # Creating loop to visit each node
#     m = queue.pop(0)
#     print (m, end = " ")
#
#     for neighbour in graph[m]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)
#
# # Driver Code
# print("Following is the Breadth-First Search")
# bfs(visited, graph, '5')    # function calling

def bfs(source: Node):
    queue = []
    queue.append(source)
    while queue:
        current_node = queue.pop(0)
        print(f"Inspecting: {current_node}")
        for neighbour in current_node.neighbours:
            if current_node.steps_from_start + 1 < neighbour.steps_from_start:
                neighbour.steps_from_start = current_node.steps_from_start + 1
                neighbour.came_from = current_node
                queue.append(neighbour)

def first(filename):
    char_grid = []
    with open(filename, "r") as f:
        for line in f:
            row = [char for char in line.strip()]
            char_grid.append(row)

    nodes_grid = []
    source_node = None
    destination_node = None
    for row in range(len(char_grid)):
        nodes_row = []
        for col in range(len(char_grid[row])):
            new_node = Node(char_grid[row][col])
            if char_grid[row][col] == "S":
                new_node.is_source = True
                source_node = new_node
            if char_grid[row][col] == "E":
                new_node.is_destination = True
                destination_node = new_node
            nodes_row.append(new_node)
        nodes_grid.append(nodes_row)

    #now find neighbours
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

            print(nodes_grid[row][col], f"potential neighbours: {[n.get_char_value() for n in potential_neighbours]}")
            print(source_node)
            print(destination_node)

    bfs(source_node)
    # node = destination_node
    # n_path = []
    # while node != source_node:
    #     n_path.append(node.came_from.get_char_value())
    #     node = node.came_from
    # print(n_path)
    # print(len(n_path))
    return destination_node.steps_from_start



def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))
