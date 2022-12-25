from importlib import import_module
from time import perf_counter
from pathlib import Path
from helpers import timer, time_str


def bench_all():
    start = perf_counter()
    day = 1
    while Path(f"day{day}").exists():
        module = import_module(f"day{day}.solution")

        print(f"Day {day}" + ("" if day > 9 else " ") , end="")

        data, refacor_time = timer(module.parse)(f"day{day}/input.txt")
        print(" | Parse: " + " " * (10 - len(time_str(refacor_time))) + f"{time_str(refacor_time)}", end="")

        _, part1_time = timer(module.part1)(data)
        print(" | Part 1: " + (" " * (10 - len(time_str(part1_time)))) + f"{time_str(part1_time)}", end="")

        _, part2_time = timer(module.part2)(data)
        print(" | Part 2: " + (" " * (10 - len(time_str(part2_time)))) + f"{time_str(part2_time)}", end="")

        total_time = refacor_time + part1_time + part2_time
        print(" | Total: " + (" " * (10 - len(time_str(total_time)))) + f"{time_str(total_time)}", end="")
        
        running_total = perf_counter() - start
        print(" | Running total: " + (" " * (10 - len(time_str(running_total)))) + f"{time_str(running_total)}")

        day += 1

def bench_day(day):
    module = import_module(f"day{day}.solution")

    data, refacor_time = timer(module.parse)(f"day{day}/input.txt")
    print(f"Parse - {time_str(refacor_time)}")

    _, part1_time = timer(module.part1)(data)
    print(f"Part1 - {time_str(part1_time)}")

    _, part2_time = timer(module.part2)(data)
    print(f"Part2 - {time_str(part2_time)}")

    print(f"Total - {time_str(refacor_time + part1_time + part2_time)}")
    print()

def bench_part1(day):
    module = import_module(f"day{day}.solution")
    data, _ = timer(module.parse)(f"day{day}/input.txt")
    _, part1_time = timer(module.part1)(data)
    print(f"Part1 - {time_str(part1_time)}")

def bench_part2(day):
    module = import_module(f"day{day}.solution")
    data, _ = timer(module.parse)(f"day{day}/input.txt")
    _, part2_time = timer(module.part2)(data)
    print(f"Part2 - {time_str(part2_time)}")


if __name__ == "__main__":
    print("To benchmark a solution, run 'python run.py bench DAY ['part1', 'part2']'")