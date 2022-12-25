from importlib import import_module
from helpers import timer, time_str


def dev_day(day):
    module = import_module(f"day{day}.solution")

    print(f"Refactor")
    data, refacor_time = timer(module.parse)(f"day{day}/input.txt")
    print(f"Time: {time_str(refacor_time)}")
    print()

    print("Part 1")
    part1_res, part1_time = timer(module.part1)(data)
    print(f"Time:   {time_str(part1_time)}")
    print(f"Result: {part1_res}")
    print()

    print("Part 2")
    part2_res, part2_time = timer(module.part2)(data)
    print(f"Time:   {time_str(part2_time)}")
    print(f"Result: {part2_res}")
    print()

    print(f"Total time: {time_str(refacor_time + part1_time + part2_time)}")
    print()

def dev_part1(day):
    module = import_module(f"day{day}.solution")
    data, _ = timer(module.parse)(f"day{day}/input.txt")
    part1_res, part1_time = timer(module.part1)(data)
    print(f"Time:   {time_str(part1_time)}")
    print(f"Result: {part1_res}")
    print()

def dev_part2(day):
    module = import_module(f"day{day}.solution")
    data, _ = timer(module.parse)(f"day{day}/input.txt")
    part2_res, part2_time = timer(module.part2)(data)
    print(f"Time:   {time_str(part2_time)}")
    print(f"Result: {part2_res}")
    print()


if __name__ == "__main__":
    print("To test a solution while deving, run 'python run.py dev DAY ['part1', 'part2']'")