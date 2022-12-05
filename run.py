import sys
from importlib import import_module
from time import perf_counter

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

if len(sys.argv) < 2:
    print("Need to specify which day you want to run")
    sys.exit()
day = int(sys.argv[1])

module = import_module(f"day{day}.solution")
parse = getattr(module, "parse")
part1 = getattr(module, "part1")
part2 = getattr(module, "part2")

data, refacor_time = timer(parse)()
part1_res, part1_time = timer(part1)(data)
part2_res, part2_time = timer(part2)(data)

print(f"Refactor")
print(f"Time: {time_str(refacor_time)}")
print()

print("Part 1")
print(f"Time:   {time_str(part1_time)}")
print(f"Result: {part1_res}")
print()

print("Part 2")
print(f"Time:   {time_str(part2_time)}")
print(f"Result: {part2_res}")
print()

print(f"Total time: {time_str(refacor_time + part1_time + part2_time)}")
print()