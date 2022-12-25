import sys
from bench import *
from dev import *

def bench_solutions():
    if len(sys.argv) < 3:
        print("You need to specify which day(s) to bench")
        return
    if sys.argv[2].isnumeric() and not 1 <= int(sys.argv[2]) <= 25:
        print("The argument should be a number between 1-25 or 'all'")
        return 
    if len(sys.argv) > 3 and sys.argv[3].lower() != "part1" and sys.argv[3].lower() != "part2":
        print("Third argument should be either 'part1' or 'part2'")
        return

    day = sys.argv[2].lower()
    if day == "all":
        bench_all()
    elif len(sys.argv) == 3:
        bench_one(int(day))
    elif sys.argv[3] == "part1":
        bench_part1(int(day))
    elif sys.argv[3] == "part2":
        bench_part2(int(day))

def assert_solutions():
    pass

def dev_solutions():
    if len(sys.argv) < 3:
        print("You need to specify which day(s) to bench")
        return
    if not sys.argv[2].isnumeric() or not 1 <= int(sys.argv[2]) <= 25:
        print("The argument should be a number between 1-25 or")
        return 
    if len(sys.argv) > 3 and sys.argv[3].lower() not in ("part1", "part2", "test"):
        print("Third argument should be either 'part1', 'part2' or 'test'")
        return

    day = int(sys.argv[2].lower())
    use_test_data = len(sys.argv) == 4 and sys.argv[3].lower() == "test" or len(sys.argv) == 5 and sys.argv[4].lower() == "test"
    if len(sys.argv) < 5:
        dev_day(day, use_test_data)
    elif sys.argv[3] == "part1":
        dev_part1(day, use_test_data)
    elif sys.argv[3] == "part2":
        dev_part2(day, use_test_data)

def main():
    if len(sys.argv) < 2:
        print("Need to specify which action to perform. The options are:")
        print("bench  - times the solutions for the given day")
        print("assert - tests the solutions for the given day")
        print("dev    - used when writing a solution")
    elif sys.argv[1].lower() == "bench":
        bench_solutions()
    elif sys.argv[1].lower() == "assert":
        assert_solutions()
    elif sys.argv[1].lower() == "dev":
        dev_solutions()
    else:
        print(f"{sys.argv[1]} is not a recognized action. The options are:")
        print("bench  - times the solutions for the given day")
        print("assert - tests the solutions for the given day")
        print("dev    - used when writing a solution")

if __name__ == "__main__":
    main()
