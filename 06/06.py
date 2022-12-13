def first(filename):
    with open(filename, "r") as f:
        line = f.readline()
        for i in range(4, len(line)):
            sequence = line[i - 4: i]
            unique_chars_number = len(set(sequence))
            # print(sequence, i)
            if unique_chars_number == 4:
                return i
def second(filename):
    with open(filename, "r") as f:
        line = f.readline()
        # print(line, len(line))
        for i in range(14, len(line)):
            sequence = line[i - 14: i]
            unique_chars_number = len(set(sequence))
            # print(sequence, i, unique_chars_number)
            if unique_chars_number == 14:
                return i

if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
