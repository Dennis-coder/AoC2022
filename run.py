import sys
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

def bench_one(day):
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

def bench_part1(day):
    module = import_module(f"day{day}.solution")
    data, _ = timer(module.parse)(f"day{day}/input.txt")
    
    print("Part 1")
    part1_res, part1_time = timer(module.part1)(data)
    print(f"Time:   {time_str(part1_time)}")
    print(f"Result: {part1_res}")
    print()

def bench_part2(day):
    module = import_module(f"day{day}.solution")
    data, _ = timer(module.parse)(f"day{day}/input.txt")
    
    print("Part 2")
    part2_res, part2_time = timer(module.part2)(data)
    print(f"Time:   {time_str(part2_time)}")
    print(f"Result: {part2_res}")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Need to specify which day you want to run")
    elif sys.argv[1].lower() == "all":
        bench_all()
    elif not sys.argv[1].isnumeric() or not (1 <= int(sys.argv[1]) <= 25):
        print("The argument should be a number between 1-25 or 'all'")
    elif len(sys.argv) == 2:
        bench_one(int(sys.argv[1]))
    elif sys.argv[2] == "part1":
        bench_part1(int(sys.argv[1]))
    elif sys.argv[2] == "part2":
        bench_part2(int(sys.argv[1]))
