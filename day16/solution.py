from pathlib import Path
import re
from queue import Queue
from dataclasses import dataclass
from functools import total_ordering
from typing import Set, List
from heapq import heappop, heappush


@total_ordering
@dataclass
class State1:
    valve: str
    ppm: int
    pressure: int
    opened: Set
    minutes: int
    estimated_pressure: int

    def open_valve(self, data, max_ppm) -> 'State1':
        return State1(
            self.valve,
            self.ppm + data[self.valve][FLOW_RATE],
            self.pressure,
            {self.valve, *self.opened},
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def move_to(self, valve, max_ppm) -> 'State1':
        return State1(
            valve,
            self.ppm,
            self.pressure,
            self.opened,
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def all_opened(self) -> 'State1':
        return State1(
            self.valve, 
            self.ppm, 
            self.pressure + self.ppm * self.minutes, 
            self.opened, 
            0, 
            self.pressure + self.ppm * self.minutes
        )

    def __lt__(self, other: 'State1'):
        return self.estimated_pressure > other.estimated_pressure

@total_ordering
@dataclass
class State2:
    valve1: str
    valve2: str
    ppm: int
    pressure: int
    opened: Set
    minutes: int
    estimated_pressure: int

    def open_both_valves(self, data, max_ppm) -> 'State2':
        return State2(
            self.valve1,
            self.valve2,
            self.ppm + data[self.valve1][FLOW_RATE] + data[self.valve2][FLOW_RATE],
            self.pressure,
            {self.valve1, self.valve2, *self.opened},
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def open_valve1_move_valve2(self, valve2, data, max_ppm) -> 'State2':
        return State2(
            self.valve1,
            valve2,
            self.ppm + data[self.valve1][FLOW_RATE],
            self.pressure,
            {self.valve1, *self.opened},
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def move_valve1_open_valve2(self, valve1, data, max_ppm) -> 'State2':
        return State2(
            valve1,
            self.valve2,
            self.ppm + data[self.valve2][FLOW_RATE],
            self.pressure,
            {self.valve2, *self.opened},
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def move_both_valves(self, valve1, valve2, max_ppm) -> 'State2':
        return State2(
            valve1,
            valve2,
            self.ppm,
            self.pressure,
            self.opened,
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def all_opened(self) -> 'State2':
        return State2(
            self.valve1, 
            self.valve2, 
            self.ppm, 
            self.pressure + self.ppm * self.minutes, 
            self.opened, 
            0, 
            self.pressure + self.ppm * self.minutes
        )

    def __lt__(self, other: 'State2'):
        return self.estimated_pressure > other.estimated_pressure

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

FLOW_RATE = "flow_rate"
CONNECTIONS = "connections"
def parse():
    with open(get_path(), "r") as file:
        data = {
            name: {
                FLOW_RATE: int(flow_rate), 
                CONNECTIONS: connections
            } for name, flow_rate, *connections in (
                re.findall("[A-Z]{2}|\d+", line) 
                for line in file.read().split("\n")
            )
        }
    return data

def part1(data):
    valves = sum([1 for valve in data.values() if valve[FLOW_RATE]])
    max_ppm = sum([valve[FLOW_RATE] for valve in data.values()])

    heap: List[State1] = [State1("AA", 0, 0, set(), 30, max_ppm * 30)]
    while len(heap):
        state = heappop(heap)
        if state.minutes == 0:
            return state.pressure
        if len(state.opened) == valves:
            heappush(heap, state.all_opened())
            continue

        state.minutes -= 1
        state.pressure += state.ppm

        if state.valve not in state.opened \
        and data[state.valve][FLOW_RATE]:
            heappush(heap, state.open_valve(data, max_ppm))

        for valve in data[state.valve][CONNECTIONS]:
            heappush(heap, state.move_to(valve, max_ppm))

def part2(data):
    valves = sum([1 for valve in data.values() if valve[FLOW_RATE]])
    max_ppm = sum([valve[FLOW_RATE] for valve in data.values()])

    heap: List[State2] = [State2("AA", "AA", 0, 0, set(), 26, max_ppm * 26)]
    while len(heap):
        state = heappop(heap)
        if state.minutes == 0:
            return state.pressure
        if len(state.opened) == valves:
            heappush(heap, state.all_opened())
            continue

        state.minutes -= 1
        state.pressure += state.ppm

        if state.valve1 not in state.opened \
        and data[state.valve1][FLOW_RATE] \
        and state.valve2 not in state.opened \
        and data[state.valve2][FLOW_RATE] \
        and state.valve1 != state.valve2:
            heappush(heap, state.open_both_valves(data, max_ppm))

        if state.valve1 not in state.opened \
        and data[state.valve1][FLOW_RATE]:
            for valve2 in data[state.valve2][CONNECTIONS]:
                heappush(heap, state.open_valve1_move_valve2(valve2, data, max_ppm))

        if state.valve2 not in state.opened \
        and data[state.valve2][FLOW_RATE]:
            for valve1 in data[state.valve1][CONNECTIONS]:
                heappush(heap, state.move_valve1_open_valve2(valve1, data, max_ppm))

        for valve1 in data[state.valve1][CONNECTIONS]:
            for valve2 in data[state.valve2][CONNECTIONS]:
                heappush(heap, state.move_both_valves(valve1, valve2, max_ppm))

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))