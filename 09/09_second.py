import numpy as np

""" 9 tails, keep track of the last one"""

class ElfLine:
    move_head = {"L": np.array([-1, 0]), "R": np.array([1, 0]), "U": np.array([0, 1]), "D": np.array([0, -1])}

    def __init__(self):
        self.tails_amount = 9
        self.head = np.array([0, 0])
        self.tails = [np.array([0, 0]) for _ in range(self.tails_amount)]
        self.tail_positions = [self.tails[-1].copy()]

    def move(self, direction, steps):
        for _ in range(steps):
            self.head += self.move_head[direction]
            self.tails[0] += self.move_tail(self.head, self.tails[0])
            for i in range(1, self.tails_amount):
                self.tails[i] += self.move_tail(self.tails[i - 1], self.tails[i])
            self.tail_positions.append(self.tails[-1].copy())

    """If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one 
    step in that direction so it remains close enough: 
    Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
    """

    @staticmethod
    def move_tail(previous, current):
        neighbour_vectors = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0],
                             [1, 1], [-1, -1], [-1, 1], [1, -1]]
        vector = previous - current
        if vector.tolist() in neighbour_vectors:
            vector = np.array([0, 0])
        else:
            vector = np.sign(vector)
        return vector

    def move_tails(self):
        pass

    def get_head_position(self):
        return self.head

    def check_if_tail_was_here(self):
        for x, y in self.tail_positions:
            if x == self.tails[0] and y == self.tails[1]:
                return True
        return False

    def get_tail_moves(self):
        unique_positions = []
        for x, y in self.tail_positions:
            unique = True
            for x_u, y_u in unique_positions:
                if x == x_u and y == y_u:
                    unique = False
            if unique:
                unique_positions.append(np.array([x, y]))
        return len(unique_positions)


def second(filename):
    elf_line = ElfLine()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            direction, steps = line[0], int(line[1])
            # print(direction, steps)
            elf_line.move(direction, steps)
            # print(elf_line.tails)

    print(f"head: {elf_line.head}")
    print(f"tail: {elf_line.tails}")
    return elf_line.get_tail_moves()


if __name__ == "__main__":
    print(second("example.txt"))
    print(second("example_2.txt"))
    print(second("input.txt"))

