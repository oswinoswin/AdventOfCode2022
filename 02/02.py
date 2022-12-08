def you_win(your_points, opponent_points):
    if your_points == 3 and opponent_points == 2:
        return True
    if your_points == 2 and opponent_points == 1:
        return True
    if your_points == 1 and opponent_points == 3:
        return True

def draft(your_points, opponent_points):
    return your_points == opponent_points
def first(filename):
    opponent_strategy = {"A": 1, "B": 2, "C": 3}
    your_strategy = {"X": 1, "Y": 2 , "Z": 3}
    your_score = 0
    with open(filename, "r") as f:
        for line in f:
            opponent_move, your_move = line.strip().split(" ")
            print(line)
            print(f"Your points: {your_strategy[your_move]}, opponent: {opponent_strategy[opponent_move]}")
            if you_win(your_strategy[your_move], opponent_strategy[opponent_move]):
                your_score += 6
                print("you win + 6")
            if draft(your_strategy[your_move], opponent_strategy[opponent_move]):
                your_score += 3
                print("Draft + 3")
            your_score += your_strategy[your_move]
    return your_score


def second(filename):
    opponent_strategy = {"A": 1, "B": 2, "C": 3}
    match_output = {"X": 0, "Y": 3, "Z": 6}
    winning_move = {1:2, 2:3, 3:1 }
    loosing_moove = {1:3, 2:1, 3:2}
    your_score = 0
    with open(filename, "r") as f:
        for line in f:
            opponent, result_code = line.strip().split(" ")
            result = match_output[result_code]
            opponent_points = opponent_strategy[opponent]
            if result == 0:
                your_score += loosing_moove[opponent_points]
            if result == 3:
                your_score += opponent_points + 3
            if result == 6:
                your_score += winning_move[opponent_points] + 6
    return your_score

if __name__ == "__main__":
    # print(first("example.txt"))

    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
