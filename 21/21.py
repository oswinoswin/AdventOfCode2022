def first(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
