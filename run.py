import sys
from importlib import import_module

if len(sys.argv) < 2:
    print("Need to specify which day you want to run")
    sys.exit()

day = int(sys.argv[1])

module = import_module(f"day{day}.solution")
refactor_data = getattr(module, "refactor_data")
part_1 = getattr(module, "part_1")
part_2 = getattr(module, "part_2")

with open(f"day{day}/indata.txt", "r") as file:
    data = refactor_data(file.read())


print(part_1(data))
print(part_2(data))