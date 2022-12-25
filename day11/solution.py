from math import prod


def parse(file_name):
    with open(file_name, "r") as file:
        data = [
            (
                [], 
                "".join(monkey_data[2].replace("Operation: new = ", "").split()), 
                int(monkey_data[3].split()[-1]), 
                int(monkey_data[4].split()[-1]), 
                int(monkey_data[5].split()[-1]), 
                tuple([int(item) for item in monkey_data[1].replace("Starting items: ", "").split(", ")])
            )
            for i, monkey_data in enumerate([
                monkey.splitlines() 
                for monkey in file.read().split("\n\n")
            ])
        ]
    return data

def part1(monkeys):
    for items, *_, start_items in monkeys:
        items.clear()
        items += list(start_items)

    inspections = [0] * len(monkeys)
    for _ in range(20):
        for i, (items, op_str, test_op, if_true, if_false, _) in enumerate(monkeys):
            inspections[i] += len(items)
            for old in items:
                new = eval(op_str) // 3
                to_monkey = if_true if new % test_op == 0 else if_false
                monkeys[to_monkey][0].append(new)
            items.clear()
    nr_of_inspections = sorted(inspections, reverse=True)
    return nr_of_inspections[0] * nr_of_inspections[1]


def part2(monkeys):
    for items, *_, start_items in monkeys:
        items.clear()
        items += list(start_items)

    lcd = prod([monkey[2] for monkey in monkeys])
    inspections = [0] * len(monkeys)
    for _ in range(10000):
        for i, (items, op_str, test_op, if_true, if_false, _) in enumerate(monkeys):
            inspections[i] += len(items)
            for old in items:
                new = eval(op_str) % lcd
                to_monkey = if_true if new % test_op == 0 else if_false
                monkeys[to_monkey][0].append(new)
            items.clear()
    nr_of_inspections = sorted(inspections, reverse=True)
    return nr_of_inspections[0] * nr_of_inspections[1]
