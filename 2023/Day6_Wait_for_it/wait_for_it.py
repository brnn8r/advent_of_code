import sys
sys.path.append('../utils')

from input_loader import InputLoader
from typing import List
from boat_race import parse_boat_race, BoatRace
from toy_boat import ToyBoat

def wait_for_it():
    print("Day6: Wait for it")

    test_data = InputLoader("test_input.txt").get_input_lines()
    test_races: List[BoatRace] = [parse_boat_race(input_line) for input_line in test_data]
    print(f"TEST1: Total winning ways: {calculate_way_of_winning(test_races)}")

    data = InputLoader().get_input_lines()
    races: List[BoatRace] = [parse_boat_race(input_line) for input_line in data]
    print(f"PART1: Total winning ways: {calculate_way_of_winning(races)}")

    test2_data = InputLoader("test2_input.txt").get_input_lines()
    test2_races: List[BoatRace] = [parse_boat_race(input_line) for input_line in test2_data]
    print(f"TEST2: Total winning ways: {calculate_way_of_winning(test2_races)}")

    data2 = InputLoader("input2.txt").get_input_lines()
    races2: List[BoatRace] = [parse_boat_race(input_line) for input_line in data2]
    print(f"PART2: Total winning ways: {calculate_way_of_winning(races2)}")


def calculate_way_of_winning(races: List[BoatRace]) -> int:
    ways_of_winning=1

    for race in races:
        winning_boats = []
        for duration in range(1, race.time - 1):
            boat = ToyBoat(duration)
            remaining_time = race.time - duration

            if boat.distance_travelled(remaining_time) > race.distance:
                winning_boats.append(boat)

            if race.distance - (boat.velocity * remaining_time) >0 and len(winning_boats) > 0:
                break

        ways_of_winning = ways_of_winning * len(winning_boats)

    return ways_of_winning

if __name__ == "__main__":
    wait_for_it()
