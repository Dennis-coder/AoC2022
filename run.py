import sys
from importlib import import_module
from time import perf_counter
from pathlib import Path

def timer(fn):
    def inner_timer(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        stop = perf_counter()
        return result, stop - start
    
    return inner_timer

def time_str(time):
    switch = {
        0: "s",
        1: "ms",
        2: "us",
        3: "ns",

    }
    i = 0
    while time < 1:
        time *= 1000
        i += 1
    
    return f"{time:.3f}{switch[i]}"

def bench_all():
    start = perf_counter()
    day = 1
    while Path(f"day{day}").exists():
        module = import_module(f"day{day}.solution")
        parse = getattr(module, "parse")
        part1 = getattr(module, "part1")
        part2 = getattr(module, "part2")

        print(f"Day {day}" + ("" if day > 9 else " ") , end="")

        data, refacor_time = timer(parse)()
        print(" | Parse: " + " " * (10 - len(time_str(refacor_time))) + f"{time_str(refacor_time)}", end="")

        _, part1_time = timer(part1)(data)
        print(" | Part 1: " + (" " * (10 - len(time_str(part1_time)))) + f"{time_str(part1_time)}", end="")

        _, part2_time = timer(part2)(data)
        print(" | Part 2: " + (" " * (10 - len(time_str(part2_time)))) + f"{time_str(part2_time)}", end="")

        total_time = refacor_time + part1_time + part2_time
        print(" | Total: " + (" " * (10 - len(time_str(total_time)))) + f"{time_str(total_time)}", end="")
        
        running_total = perf_counter() - start
        print(" | Running total: " + (" " * (10 - len(time_str(running_total)))) + f"{time_str(running_total)}")

        day += 1

def bench_one(day):
    module = import_module(f"day{day}.solution")
    parse = getattr(module, "parse")
    part1 = getattr(module, "part1")
    part2 = getattr(module, "part2")

    print(f"Refactor")
    data, refacor_time = timer(parse)()
    print(f"Time: {time_str(refacor_time)}")
    print()

    print("Part 1")
    part1_res, part1_time = timer(part1)(data)
    print(f"Time:   {time_str(part1_time)}")
    print(f"Result: {part1_res}")
    print()

    print("Part 2")
    part2_res, part2_time = timer(part2)(data)
    print(f"Time:   {time_str(part2_time)}")
    print(f"Result: {part2_res}")
    print()

    print(f"Total time: {time_str(refacor_time + part1_time + part2_time)}")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Need to specify which day you want to run")
    elif sys.argv[1].lower() == "all":
        bench_all()
    elif not sys.argv[1].isnumeric():
        print("The argument should be a number between 1-25 or 'all'")
    else:
        bench_one(int(sys.argv[1]))
