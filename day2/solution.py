def parse(file_name):
    with open(file_name, "r") as file:
        data = [
            (ord(x[0])-65, ord(x[2])-88) 
            for x in file.read().split("\n")
        ]
    return data

def part1(data):
    score = 0
    for op, you in data:
        score += (you + 1)
        if (op + 1) % 3 == you:
            score += 6
        elif op == you:
            score += 3
    return score

def part2(data):
    score = 0
    for op, res in data:
        score += res * 3
        if res == 2:
            score += (op + 1) % 3 + 1
        elif res == 1:
            score += op + 1
        else:
            score += (op + 2) % 3 + 1
    return score
