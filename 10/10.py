
def first(filename):
    check_points = {20, 60, 100, 140, 180, 220}
    with open(filename, "r") as f:
        cycle = 0
        x = 1
        signal_sum = 0
        for line in f:
            if line.startswith("noop"):
                cycle += 1
                if cycle in check_points:
                    signal = cycle*x
                    print(f"CHECKPOINT: {cycle}, signal: {signal}")
                    signal_sum += signal
                print(f"After {cycle} cycle X = {x}")
            else:
                line = line.strip().split(" ")
                operation, value = line[0], int(line[1]) #only add operations
                cycle += 1
                if cycle in check_points:
                    signal = cycle*x
                    print(f"CHECKPOINT: {cycle}, signal: {signal}")
                    signal_sum += signal
                print(f"After {cycle} cycle X = {x}")
                cycle += 1
                if cycle in check_points:
                    signal = cycle*x
                    print(f"CHECKPOINT: {cycle}, signal: {signal}")
                    signal_sum += signal
                x += value
                print(f"After {cycle} cycle X = {x}")
        return signal_sum


def draw_crt(crt_string, cycle, x):
    if cycle in {40, 80, 120, 160, 200}:
        crt_string = crt_string + "\n"
    crt_position = cycle % 40
    if crt_position- 1 <= x <= crt_position + 1:
        return crt_string + "#"
    return crt_string + "."


def second(filename):
    with open(filename, "r") as f:
        cycle = -1
        x = 1
        crt_string = ""
        for line in f:
            if line.startswith("noop"):
                cycle += 1
                crt_string = draw_crt(crt_string, cycle, x)
            else:
                line = line.strip().split(" ")
                operation, value = line[0], int(line[1]) #only add operations
                cycle += 1
                crt_string = draw_crt(crt_string, cycle, x)
                cycle += 1
                crt_string = draw_crt(crt_string, cycle, x)
                x += value
        return crt_string


if __name__ == "__main__":
    # print(first("example_smol.txt"))
    # print(first("example.txt"))
    # print(first("input.txt"))
    # print(second("example.txt"))
    print(second("input.txt"))
