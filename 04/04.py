def are_totally_overlapping(min1, max1, min2, max2):
    # check if elf1 is in range of elf2
    if min1 >= min2 and max1 <= max2:
        return True
    # check if elf2 is in range of elf1
    if min2 >= min1 and max2 <= max1:
        return True
    return False


def are_overlapping(min1, max1, min2, max2):
    # check if min1 is in the range of elf2
    if min2 <= min1 <= max2:
        return True
    if min2 <= max1 <= max2:
        return True
    if min1 <= min2 <= max1:
        return True
    if min1 <= max2 <= max1:
        return True
    return False


def first(filename):
    result = 0
    with open(filename, "r") as f:
        for line in f:
            e1, e2 = line.strip().split(',')
            min1, max1 = e1.split('-')
            min2, max2 = e2.split('-')
            min1 = int(min1)
            max1 = int(max1)
            min2 = int(min2)
            max2 = int(max2)
            print(e1, e2)
            if are_totally_overlapping(min1, max1, min2, max2):
                result += 1
    return result


def second(filename):
    result = 0
    with open(filename, "r") as f:
        for line in f:
            e1, e2 = line.strip().split(',')
            min1, max1 = e1.split('-')
            min2, max2 = e2.split('-')
            min1 = int(min1)
            max1 = int(max1)
            min2 = int(min2)
            max2 = int(max2)
            # print(e1, e2)
            if are_overlapping(min1, max1, min2, max2):
                result += 1
    return result


if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
