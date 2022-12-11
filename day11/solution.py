from pathlib import Path
from math import prod


class Monkey:
    def __init__(self, data: str):
        self.data = data.splitlines()
        
    def reset(self):
        self.items = [int(item) for item in self.data[1].replace("Starting items: ", "").split(", ")]
        self.op = "".join(self.data[2].replace("Operation: new = ", "").split())
        self.test_op = int(self.data[3].split()[-1])
        self.if_true = int(self.data[4].split()[-1])
        self.if_false = int(self.data[5].split()[-1])
        self.inspections = 0

    def apply_operation(self):
        self.inspections += len(self.items)
        self.items = [eval(self.op) for old in self.items]
    
    def test(self, val):
        return self.if_true if val % self.test_op == 0 else self.if_false

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [Monkey(monkey) for monkey in file.read().split("\n\n")]
    return data

def part1(monkeys):
    for monkey in monkeys:
        monkey.reset()
    for _ in range(20):
        for monkey in monkeys:
            monkey.apply_operation()
            for item in monkey.items:
                to_monkey = monkey.test(item // 3)
                monkeys[to_monkey].items.append(item // 3)
            monkey.items = []
    nr_of_inspections = sorted([x.inspections for x in monkeys], reverse=True)
    return nr_of_inspections[0] * nr_of_inspections[1]


def part2(monkeys):
    for monkey in monkeys:
        monkey.reset()
    
    lcd = prod([monkey.test_op for monkey in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            monkey.apply_operation()
            for item in monkey.items:
                to_monkey = monkey.test(item % lcd)
                monkeys[to_monkey].items.append(item % lcd)
            monkey.items = []
    nr_of_inspections = sorted([x.inspections for x in monkeys], reverse=True)
    return nr_of_inspections[0] * nr_of_inspections[1]


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))