import re


def parse(file_name):
    pattern = re.compile("(\d+)-(\d+),(\d+)-(\d+)")
    with open(file_name, "r") as file:
        data = [
            list(map(int, pair.groups()))
            for pair in re.finditer(pattern, file.read())
        ]
    return data

def part1(data):
    amount = 0
    for x1, y1, x2, y2 in data:
        if x1 <= x2 <= y2 <= y1 \
        or x2 <= x1 <= y1 <= y2:
            amount += 1
    return amount


def part2(data):
    amount = 0
    for x1, y1, x2, y2 in data:
        if x1 <= x2 <= y1 \
        or x2 <= x1 <= y2:
            amount += 1
    return amount
