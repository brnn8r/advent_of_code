from typing import List
from dataclasses import dataclass

@dataclass
class BoatRace:
    time: int
    distance: int


def parse_boat_race(input: str) -> BoatRace:
    split_input = input.strip().split(" ")

    return BoatRace(int(split_input[0]), int(split_input[1]))