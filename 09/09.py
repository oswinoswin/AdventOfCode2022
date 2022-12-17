import numpy as np


class ElfLine:
    move = {"L": np.array([-1, 0]), "R": np.array([1, 0]), "U": np.array([0, 1]), "D": np.array([0, -1])}

    def __init__(self):
        self.head = np.array([0, 0])
        self.tail = np.array([0, 0])
        self.tail_positions = [self.tail.copy()]

    def check_if_tail_was_here(self):
        for x, y in self.tail_positions:
            if x == self.tail[0] and y == self.tail[1]:
                return True
        return False

    def move_head(self, direction, steps):
        for i in range(steps):
            self.head += self.move[direction]
            self.tail += self.move_tail()
            if not self.check_if_tail_was_here():
                self.tail_positions.append(self.tail.copy())
            # print(f"h: {self.head} t: {self.tail} positions: {self.tail_positions}")

    """If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one 
    step in that direction so it remains close enough: 
    Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
    """
    def move_tail(self):
        neighbour_vectors = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0],
                             [1, 1], [-1, -1], [-1, 1], [1, -1]]
        vector = self.head - self.tail
        if vector.tolist() in neighbour_vectors:
            vector = np.array([0, 0])
        else:
            vector = np.sign(vector)
        return vector

    def get_head_position(self):
        return self.head

    def get_tail_moves(self):
        return len(self.tail_positions)


def first(filename):
    elf_line = ElfLine()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            direction, steps = line[0], int(line[1])
            # print(direction, steps)
            elf_line.move_head(direction, steps)

    print(f"head: {elf_line.head}")
    print(f"tail: {elf_line.tail}")
    return elf_line.get_tail_moves()


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))
