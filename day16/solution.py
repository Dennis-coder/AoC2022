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

    def open_valve(self, flow_rates, max_ppm) -> 'State1':
        return State1(
            self.valve,
            self.ppm + flow_rates[self.valve],
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
    
    def id(self) -> tuple:
        return (self.valve, self.ppm, self.pressure)

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

    def open_both_valves(self, flow_rates, max_ppm) -> 'State2':
        return State2(
            self.valve1,
            self.valve2,
            self.ppm + flow_rates[self.valve1] + flow_rates[self.valve2],
            self.pressure,
            {self.valve1, self.valve2, *self.opened},
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def open_valve1_move_valve2(self, valve2, flow_rates, max_ppm) -> 'State2':
        return State2(
            self.valve1,
            valve2,
            self.ppm + flow_rates[self.valve1],
            self.pressure,
            {self.valve1, *self.opened},
            self.minutes,
            self.pressure + max_ppm * self.minutes
        )
    
    def move_valve1_open_valve2(self, valve1, flow_rates, max_ppm) -> 'State2':
        return State2(
            valve1,
            self.valve2,
            self.ppm + flow_rates[self.valve2],
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

    def id(self) -> tuple:
        return ((self.valve1, self.valve2) if self.valve1 < self.valve2 else (self.valve2, self.valve1), self.ppm, self.pressure)

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = {
            name: {
                "flow_rate": int(flow_rate), 
                "tunnels": tunnels
            } for name, flow_rate, *tunnels in (
                re.findall("[A-Z]{2}|\d+", line) 
                for line in file.read().split("\n")
            )
        }
    return (
        {k: v["flow_rate"] for k, v in data.items()}, 
        {k: v["tunnels"] for k, v in data.items()}
    )

def part1(data):
    flow_rates, tunnels = data
    valves = sum([1 for flow_Rate in flow_rates.values() if flow_Rate])
    max_ppm = sum([flow_Rate for flow_Rate in flow_rates.values()])
    visited_states = set()

    heap: List[State1] = [State1("AA", 0, 0, set(), 30, max_ppm * 30)]
    while len(heap):
        state = heappop(heap)
        if state.minutes == 0:
            return state.pressure
        if state.id() in visited_states:
            continue
        visited_states.add(state.id())
        if len(state.opened) == valves:
            heappush(heap, state.all_opened())
            continue

        state.minutes -= 1
        state.pressure += state.ppm

        if state.valve not in state.opened \
        and flow_rates[state.valve]:
            heappush(heap, state.open_valve(flow_rates, max_ppm))

        for valve in tunnels[state.valve]:
            heappush(heap, state.move_to(valve, max_ppm))

def part2(data):
    flow_rates, tunnels = data
    valves = sum([1 for flow_Rate in flow_rates.values() if flow_Rate])
    max_ppm = sum([flow_Rate for flow_Rate in flow_rates.values()])
    visited_states = set()

    heap: List[State2] = [State2("AA", "AA", 0, 0, set(), 26, max_ppm * 26)]
    while len(heap):
        state = heappop(heap)
        if state.minutes == 0:
            return state.pressure
        if state.id() in visited_states:
            continue
        visited_states.add(state.id())
        if len(state.opened) == valves:
            heappush(heap, state.all_opened())
            continue

        state.minutes -= 1
        state.pressure += state.ppm

        if state.valve1 not in state.opened \
        and flow_rates[state.valve1] \
        and state.valve2 not in state.opened \
        and flow_rates[state.valve2] \
        and state.valve1 != state.valve2:
            heappush(heap, state.open_both_valves(flow_rates, max_ppm))

        if state.valve1 not in state.opened \
        and flow_rates[state.valve1]:
            for valve2 in tunnels[state.valve2]:
                heappush(heap, state.open_valve1_move_valve2(valve2, flow_rates, max_ppm))

        if state.valve2 not in state.opened \
        and flow_rates[state.valve2]:
            for valve1 in tunnels[state.valve1]:
                heappush(heap, state.move_valve1_open_valve2(valve1, flow_rates, max_ppm))

        for valve1 in tunnels[state.valve1]:
            for valve2 in tunnels[state.valve2]:
                heappush(heap, state.move_both_valves(valve1, valve2, max_ppm))

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))