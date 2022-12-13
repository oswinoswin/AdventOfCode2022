import re

def first(filename: str, stacks: list):
    with open(filename, "r") as f:
        for line in f:
            nums = re.findall(r'[0-9]+', line)
            items_to_move = int(nums[0])
            source = stacks[int(nums[1]) - 1]
            destination = stacks[int(nums[2]) - 1]
            print(line, stacks)
            for i in range(items_to_move):
                item = source.pop()
                destination.append(item)
            stacks[int(nums[1]) - 1] = source
            stacks[int(nums[2]) - 1] = destination
            print(line, stacks)
            print("\n")
        return "".join(stack[-1] for stack in stacks)


def second(filename: str, stacks: list):
    with open(filename, "r") as f:
        for line in f:
            nums = re.findall(r'[0-9]+', line)
            items_to_move = int(nums[0])
            source = stacks[int(nums[1]) - 1]
            destination = stacks[int(nums[2]) - 1]
            stacks[int(nums[1]) - 1] = source
            stacks[int(nums[2]) - 1] = destination

            print(line, stacks)

            tmp_stack = []  #could be prettier, but whatever
            for i in range(items_to_move):
                item = source.pop()
                tmp_stack.append(item)
            for i in range(items_to_move):
                item = tmp_stack.pop()
                destination.append(item)

            stacks[int(nums[1]) - 1] = source
            stacks[int(nums[2]) - 1] = destination

            print(stacks)
            print("\n")
        return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    example_stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
    # print(first("example.txt", example_stacks))
    input_stacks = [["F", "H", "B", "V", "R", "Q", "D", "P"],
                    ["L", "D", "Z", "Q", "W", "V"],
                    ["H", "L", "Z", "Q", "G", "R", "P", "C"],
                    ["R", "D", "H", "F", "J", "V", "B"],
                    ["Z", "W", "L", "C"],
                    ["J", "R", "P", "N", "T", "G", "V", "M"],
                    ["J", "R", "L", "V", "M", "B", "S"],
                    ["D", "P", "J"],
                    ["D", "C", "N", "W", "V"]]
    # print(first("input.txt", input_stacks))
    print(second("example.txt", example_stacks))
    print(second("input.txt", input_stacks))

"""    
Example stacks
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
"""

"""
My Input
[P]     [C]         [M]
[D]     [P] [B]     [V] [S]
[Q] [V] [R] [V]     [G] [B]
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]
 1   2   3   4   5   6   7   8   9

"""
