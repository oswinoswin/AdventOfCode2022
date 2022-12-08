
def find_priority(character: str):
    if character.islower():
        return ord(character) - 96
    return ord(character) - 38


def first(filename):
    result = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            first_part = line[:(len(line))//2]
            second_part = line[(len(line))//2:]
            common = set(first_part) & set(second_part)
            common_element = list(common)[0]
            result += find_priority(common_element)
    return result


def second(filename):
    result = 0
    with open(filename, "r") as f:
        while True:
            line1 = f.readline()
            if not line1:
                break
            line2 = f.readline()
            line3 = f.readline()
            line1 = line1.strip()
            line2 = line2.strip()
            line3 = line3.strip()
            common = set(line1) & set(line2) & set(line3)
            common_element = list(common)[0]
            result += find_priority(common_element)
    return result


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
