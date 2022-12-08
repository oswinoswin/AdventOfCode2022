def first(filename):
    with open(filename, "r") as f:
        elf = 1
        calories = 0
        max_calories = 0
        max_elf = 0
        for line in f:
            if line == "\n":
                if calories > max_calories:
                    max_calories = calories
                    max_elf = elf
                elf += 1
                calories = 0
                # print("Elf: " + elf)
            else:
                print(line)
                calories += int(line)

    return (max_elf, max_calories)


def second(filename):
    total_calories = []
    last_line = None
    calories = 0
    with open(filename, "r") as f:

        for line in f:
            if line == "\n":
                total_calories.append(calories)
                calories = 0
                # print("Elf: " + elf)
            else:
                print(line)
                calories += int(line)
            last_line = line
    last_line = line
    if last_line != "\n":
        total_calories.append(calories)
    total_calories.sort(reverse=True)
    print(total_calories)
    return sum(total_calories[:3])

if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))