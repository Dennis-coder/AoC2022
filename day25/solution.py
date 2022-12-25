def parse(file_name) -> list[str]:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    return data

def snafu_to_decimal(number: str) -> int:
    convert = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    return sum([
        convert[n] * 5 ** i for i, n in enumerate(reversed(number))
    ])

def dec_to_five(num: int) -> str:
    num_str = ""
    while num>0:
        num_str += str(num%5)
        num //= 5
    return num_str[::-1]

def five_to_snafu(number: str) -> str:
    convert = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
    base_five = [0] + [int(x) for x in number]

    for i in range(len(base_five) -1, -1, -1):
        if base_five[i] > 2:
            base_five[i-1] += 1
            base_five[i] -= 5

    if base_five[0] == 0:
        base_five = base_five[1:]

    return "".join([
        convert[x]
        for x in base_five
    ])

def decimal_to_snafu(number: int) -> str:
    return five_to_snafu(dec_to_five(number))

def part1(data):
    return decimal_to_snafu(sum([
        snafu_to_decimal(num)
        for num in data
    ]))

def part2(data):
    return "there is not part 2, the advent calendar is complete"
