from pathlib import Path
import re
from math import ceil, prod


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    pattern = re.compile("Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")
    with open(get_path(), "r") as file:
        data = [
            [
                int(x) 
                for x in re.fullmatch(pattern, line).groups()
            ]
            for line in file.read().split("\n")
        ]
    return data

def buy_robot(robots, ore=False, clay=False, obsidian=False, geode=False):
        return (robots[0] + ore, robots[1] + clay, robots[2] + obsidian, robots[3] + geode)

def update_materials(materials, robots, time, ore=0, clay=0, obsidian=0):
    return (
        materials[0] + robots[0] * time - ore,
        materials[1] + robots[1] * time - clay,
        materials[2] + robots[2] * time - obsidian,
        materials[3] + robots[3] * time
    )

def recursive(bp, time_limit):
    def inner(time_left, robots, materials) -> int:
        nonlocal max_geodes

        key = (*robots, *materials)
        if key in time_memoization and time_left <= time_memoization[key]:
            return
        time_memoization[key] = time_left

        key = (time_left, *robots, *materials[:3])
        if key in geode_memoization and materials[3] <= geode_memoization[key]:
            return
        geode_memoization[key] = materials[3]

        if time_left == 0: return 
        if materials[3] + robots[3] * time_left + time_left * (time_left + 1) // 2 < max_geodes: return

        max_geodes = max(max_geodes, materials[3] + robots[3] * time_left)

        if robots[0] < max_ore: # buy ore-collecting robot
            time_needed = max(
                ceil((ore_cost - materials[0]) / robots[0]),
                0
            ) + 1
            if time_needed <= time_left:
                inner(
                    time_left - time_needed,
                    buy_robot(robots, ore=True),
                    update_materials(materials, robots, time_needed, ore=ore_cost)
                )
            
        if robots[1] < max_clay: # buy clay-collecting robot
            time_needed = max(
                ceil((clay_cost - materials[0]) / robots[0]),
                0
            ) + 1
            if time_needed <= time_left:
                inner(time_left - time_needed,
                    buy_robot(robots, clay=True),
                    update_materials(materials, robots, time_needed, ore=clay_cost)
                )
        
        if robots[1] and robots[2] < max_obsidian: # buy obsidian-collecting robot
            time_needed = max(
                ceil((obsidian_ore_cost - materials[0]) / robots[0]),
                ceil((obsidian_clay_cost - materials[1]) / robots[1]),
                0
            ) + 1
            if time_needed <= time_left:
                inner(time_left - time_needed,
                    buy_robot(robots, obsidian=True),
                    update_materials(materials, robots, time_needed, ore=obsidian_ore_cost, clay=obsidian_clay_cost)
                )

        if robots[2]: # buy geode-cracking robot
            time_needed = max(
                ceil((geode_ore_cost - materials[0]) / robots[0]),
                ceil((geode_obsidian_cost - materials[2]) / robots[2]),
                0
            ) + 1
            if time_needed <= time_left:
                inner(time_left - time_needed,
                    buy_robot(robots, geode=True),
                    update_materials(materials, robots, time_needed, ore=geode_ore_cost, obsidian=geode_obsidian_cost)
                )
        
    ore_cost, clay_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost = bp
    max_geodes = 0
    max_ore = max(ore_cost, clay_cost, obsidian_ore_cost, geode_ore_cost)
    max_clay = obsidian_clay_cost
    max_obsidian = geode_obsidian_cost
    time_memoization = {}
    geode_memoization = {}
    inner(time_limit, (1,0,0,0), (0,0,0,0))
    return max_geodes

def part1(data):
    return sum([id * recursive(bp, 24) for id, *bp in data])

def part2(data):  
    return prod([recursive(bp, 32) for _, *bp in data[:3]])


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))