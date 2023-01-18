import re


class Monkey:
    def __init__(self, lines: list, operation):
        self.monkey_id = int(re.findall(r"\d+", lines[0])[0])
        self.items = [int(x) for x in re.findall(r"\d+", lines[1])]
        self.operation = operation
        self.test_var = int(re.findall(r"\d+", lines[3])[0])
        self.if_true = int(re.findall(r"\d+", lines[4])[0])
        self.if_false = int(re.findall(r"\d+", lines[5])[0])
        self.inspections_counter = 0

    def __str__(self):
        return str(self.__dict__)

    def inspect_item(self, item):
        self.inspections_counter += 1
        worry_level = self.operation(item)
        worry_level = worry_level // 100
        if worry_level % self.test_var == 0:
            return self.if_true, worry_level
        else:
            return self.if_false, worry_level

    def add(self, item):
        self.items.append(item)

    def play_turn(self):
        results = []
        while self.items:
            item = self.items.pop(0)
            next_monkey, new_worry_level = self.inspect_item(item)
            results.append([next_monkey, new_worry_level])
        return results


def first(filename, monkey_amount, functions_list):
    monkey_list = []
    with open(filename, "r") as f:
        for i in range(monkey_amount - 1):
            monkey_str = [next(f).strip() for x in range(7)]
            monkey = Monkey(monkey_str, functions_list[i])
            monkey_list.append(monkey)
        monkey_str = [next(f).strip() for x in range(6)] # ugly read of last elem
        monkey = Monkey(monkey_str, functions_list[-1])
        monkey_list.append(monkey)

        for r in range(10000):
            print(f"Round: {r}")
            for monkey in monkey_list:
                results = monkey.play_turn()
                for next_monkey, item in results:
                    monkey_list[next_monkey].add(item)
        monkey_list.sort(key=lambda x: x.inspections_counter, reverse=True)
        return monkey_list[0].inspections_counter * monkey_list[1].inspections_counter



def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt", 4, [lambda x: x*19, lambda x: x + 6, lambda x: x*x, lambda x: x + 3]))
    # print(first("input.txt", 8, [lambda x: x*3, lambda x: x + 1, lambda x: x*13, lambda x: x*x,
    #                              lambda x: x + 7, lambda x: x + 8, lambda x: x + 4, lambda x: x + 5]))
    # print(second("example.txt"))
    # print(second("input.txt"))
