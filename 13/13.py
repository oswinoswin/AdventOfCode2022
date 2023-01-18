def compare_digits(left: str, right: str):
    print(f"\t COMPARE DIGITS: {left} vs {right}")
    left = int(left.split(",")[0])
    right = int(right.split(",")[0])
    if left < right:
        return 1
    if left > right:
        return -1
    return 0


def compare_lists(left: str, right: str):
    left_list = left[1:-1].split(',')
    right_list = right[1:-1].split(',')
    for l_i in range(len(left_list)):
        if l_i >= len(right_list):
            return - 1
        l_str = ",".join(left_list[l_i:])
        r_str = ",".join(right_list[l_i:])
        # print(f"LIST ComparePARE should go with:{l_str} AND {r_str}")
        tmp_comparison = compare(l_str, r_str)
        if tmp_comparison != 0:
            return tmp_comparison
    if len(right_list) > len(left_list):
        return 1
    return 0


def compare(left: str, right: str) -> int:
    print(f"- Compare {left} vs {right}")
    if left[0].isdigit() and right[0].isdigit():
        print(f"\t- Compare digits = {compare_digits(left, right)}")
        return compare_digits(left, right)
    if left.startswith("[") and right.startswith("["):
        # print(f"\t- Compare two lists: {left[1:-1].split(',')} | {right[1:-1].split(',')}")
        return compare_lists(left, right)
    if left.startswith("[") and not right.startswith("["):
        new_right = f"[{right}]"
        # print(f"Mixed type! convert right to {new_right}")
        return compare(left, new_right)
    if not left.startswith("[") and right.startswith("["):
        new_left = f"[{left}]"
        # print(f"Mixed type, convert left to: {new_left}")
        return compare(new_left, right)
    return 0


def first(filename):
    with open(filename, "r") as f:
        pair_index = 1
        while True:
            left = f.readline().strip()
            right = f.readline().strip()
            print(f"{pair_index} left = {left.split(',')}, right = {right.split(',')}")
            print(compare(left, right))
            line = f.readline()
            pair_index += 1
            if not line:
                break


def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    # print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))
