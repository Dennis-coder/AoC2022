from pathlib import Path
import re
from collections import namedtuple
from math import ceil
from typing import List
import heapq

Blueprint = namedtuple("Blueprint", "id,ore_robot_cost,clay_robot_cost,obsidian_robot_ore_cost,obsidian_robot_clay_cost,geode_robot_ore_cost,geode_robot_obsidian_cost")

State = namedtuple("State", "ore_robots,clay_robots,obsidian_robots,geode_robots,ores,clay,obsidian,geodes,time_left,prev")

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
            Blueprint(
                *[
                    int(x) 
                    for x in re.fullmatch(pattern, line).groups()
                ]
            ) 
            for line in file.read().split("\n")
        ]
    return data

def part1(data: List[Blueprint]):
    sum_quality_levels = 0

    for bp in data:
        max_geodes = 0
        dfs = [State(1, 0, 0, 0, 0, 0, 0, 0, 24, None)]
        max_ore_robots = max(bp.ore_robot_cost, bp.clay_robot_cost, bp.obsidian_robot_ore_cost, bp.geode_robot_ore_cost)
        max_clay_robots = bp.obsidian_robot_clay_cost
        max_obsidian_robots = bp.geode_robot_obsidian_cost
        while len(dfs):
            state = dfs.pop()
            max_geodes = max(max_geodes, state.geodes + state.geode_robots * state.time_left)
            
            if state.ore_robots and state.ore_robots < max_ore_robots: # buy ore-collecting robot
                ore_needed = bp.ore_robot_cost - state.ores
                time_needed = ceil(ore_needed / state.ore_robots) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        ore_robots=state.ore_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.ore_robot_cost,
                        clay=state.clay + state.clay_robots * time_needed,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))
            
            if state.ore_robots and state.clay_robots < max_clay_robots: # buy clay-collecting robot
                ore_needed = bp.clay_robot_cost - state.ores
                time_needed = ceil(ore_needed / state.ore_robots) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        clay_robots=state.clay_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.clay_robot_cost,
                        clay=state.clay + state.clay_robots * time_needed,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))
            
            if state.ore_robots and state.clay_robots and state.obsidian_robots < max_obsidian_robots: # buy obsidian-collecting robot
                ore_needed = bp.obsidian_robot_ore_cost - state.ores
                clay_needed = bp.obsidian_robot_clay_cost - state.clay
                time_needed = max(
                    ceil(ore_needed / state.ore_robots),
                    ceil(clay_needed / state.clay_robots)
                ) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        obsidian_robots=state.obsidian_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.obsidian_robot_ore_cost,
                        clay=state.clay + state.clay_robots * time_needed - bp.obsidian_robot_clay_cost,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))

            if state.ore_robots and state.obsidian_robots: # buy geode-cracking robot
                ore_needed = bp.geode_robot_ore_cost - state.ores
                obsidian_needed = bp.geode_robot_obsidian_cost - state.obsidian
                time_needed = max(
                    ceil(ore_needed / state.ore_robots),
                    ceil(obsidian_needed / state.obsidian_robots)
                ) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        geode_robots=state.geode_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.geode_robot_ore_cost,
                        clay=state.clay + state.clay_robots * time_needed,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed - bp.geode_robot_obsidian_cost,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))
           
        sum_quality_levels += bp.id * max_geodes

    return sum_quality_levels

def guess_geodes(state: State):
    return (
        state.geodes + 
        state.geode_robots * state.time_left +
        state.time_left * (state.time_left + 1) // 2
    )

def part2(data):
    prod = 1
    for bp in data[:3]:
        max_geodes = 0
        dfs = [State(1, 0, 0, 0, 0, 0, 0, 0, 32, None)]
        max_ore_robots = max(bp.ore_robot_cost, bp.clay_robot_cost, bp.obsidian_robot_ore_cost, bp.geode_robot_ore_cost)
        max_clay_robots = bp.obsidian_robot_clay_cost
        max_obsidian_robots = bp.geode_robot_obsidian_cost
        while len(dfs):
            state = dfs.pop()
            max_geodes = max(max_geodes, state.geodes + state.geode_robots * state.time_left)

            if guess_geodes(state) < max_geodes:
                continue

            if state.ore_robots and state.ore_robots < max_ore_robots: # buy ore-collecting robot
                ore_needed = bp.ore_robot_cost - state.ores
                time_needed = ceil(ore_needed / state.ore_robots) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        ore_robots=state.ore_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.ore_robot_cost,
                        clay=state.clay + state.clay_robots * time_needed,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))
            
            if state.ore_robots and state.clay_robots < max_clay_robots: # buy clay-collecting robot
                ore_needed = bp.clay_robot_cost - state.ores
                time_needed = ceil(ore_needed / state.ore_robots) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        clay_robots=state.clay_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.clay_robot_cost,
                        clay=state.clay + state.clay_robots * time_needed,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))
            
            if state.ore_robots and state.clay_robots and state.obsidian_robots < max_obsidian_robots: # buy obsidian-collecting robot
                ore_needed = bp.obsidian_robot_ore_cost - state.ores
                clay_needed = bp.obsidian_robot_clay_cost - state.clay
                time_needed = max(
                    ceil(ore_needed / state.ore_robots),
                    ceil(clay_needed / state.clay_robots)
                ) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        obsidian_robots=state.obsidian_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.obsidian_robot_ore_cost,
                        clay=state.clay + state.clay_robots * time_needed - bp.obsidian_robot_clay_cost,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))

            if state.ore_robots and state.obsidian_robots: # buy geode-cracking robot
                ore_needed = bp.geode_robot_ore_cost - state.ores
                obsidian_needed = bp.geode_robot_obsidian_cost - state.obsidian
                time_needed = max(
                    ceil(ore_needed / state.ore_robots),
                    ceil(obsidian_needed / state.obsidian_robots)
                ) + 1
                time_needed = time_needed if time_needed > 0 else 1
                if state.time_left >= time_needed:
                    dfs.append(state._replace(
                        geode_robots=state.geode_robots + 1,
                        ores=state.ores + state.ore_robots * time_needed - bp.geode_robot_ore_cost,
                        clay=state.clay + state.clay_robots * time_needed,
                        obsidian=state.obsidian + state.obsidian_robots * time_needed - bp.geode_robot_obsidian_cost,
                        geodes=state.geodes + state.geode_robots * time_needed,
                        time_left=state.time_left - time_needed,
                        prev=state
                    ))
            
        prod *= max_geodes

    return prod


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))