import sys
sys.path.append('../utils')

from input_loader import InputLoader
import time
import multiprocessing
from typing import List
import functools
from lookup_map import parse_category_map, CategoryMap, CategoryLookup

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)

def seed_fertilizer():
    print("Day5: Seed Fertilizer")
    print(f"CPU Cores: {multiprocessing.cpu_count()}")

    available_cores = int(multiprocessing.cpu_count()) #/2)

    seed_data = InputLoader("input/seeds.txt").get_input_lines()
    seed_to_soil_data = InputLoader("input/seed-to-soil.txt").get_input_lines()
    soil_to_fertilizer_data = InputLoader("input/soil-to-fertilizer.txt").get_input_lines()
    fertilizer_to_water_data = InputLoader("input/fertilizer-to-water.txt").get_input_lines()
    water_to_light_data = InputLoader("input/water-to-light.txt").get_input_lines()
    light_to_temperature_data = InputLoader("input/light-to-temperature.txt").get_input_lines()
    temperature_to_humidity_data = InputLoader("input/temperature-to-humidity.txt").get_input_lines()
    humidity_to_location_data = InputLoader("input/humidity-to-location.txt").get_input_lines()

    seed_data_split = seed_data[0].split(" ")

    seeds = [int(seed) for seed in seed_data_split]
    print(seeds)

    seed_to_soil_lookup : CategoryLookup = generate_lookup("seed=>soil", seed_to_soil_data)
    soil_to_fertilizer_lookup: CategoryLookup = generate_lookup("soil=>fertilizer", soil_to_fertilizer_data)
    fertilizer_to_water_lookup: CategoryLookup = generate_lookup("fertilizier=>water", fertilizer_to_water_data)
    water_to_light_lookup: CategoryLookup = generate_lookup("water=>light", water_to_light_data)
    light_to_temperature_lookup: CategoryLookup = generate_lookup("light=>temp",light_to_temperature_data)
    temperature_to_humidity_lookup: CategoryLookup = generate_lookup("temp=>humidity",temperature_to_humidity_data)
    humidity_to_location_lookup: CategoryLookup = generate_lookup("humidity=>loc",humidity_to_location_data)

    seed_to_location = compose(humidity_to_location_lookup.map, temperature_to_humidity_lookup.map,
                               light_to_temperature_lookup.map, water_to_light_lookup.map,
                               fertilizer_to_water_lookup.map, soil_to_fertilizer_lookup.map, seed_to_soil_lookup.map)

    min_seed_location = seed_to_location(seeds[0])
    for seed in seeds:
        seed_location = seed_to_location(seed)
        min_seed_location = min(seed_location, min_seed_location)

    print(f"Part1: min location = {min_seed_location} ")

    seed_iter = iter(seed_data_split)

    seed_ranges = []
    for seed in seed_iter:
        seed_ranges.append([int(seed), int(next(seed_iter))])

    process_seed_partition_partial = functools.partial(process_seed_partition, humidity_to_location_lookup=humidity_to_location_lookup, temperature_to_humidity_lookup=temperature_to_humidity_lookup, light_to_temperature_lookup=light_to_temperature_lookup, water_to_light_lookup=water_to_light_lookup, fertilizer_to_water_lookup=fertilizer_to_water_lookup,soil_to_fertilizer_lookup=soil_to_fertilizer_lookup, seed_to_soil_lookup=seed_to_soil_lookup)

    with multiprocessing.Pool(available_cores) as p:
        p.map(process_seed_partition_partial, seed_ranges)

    #print(f"Part2: min location = {min_seed_location} ")

def process_seed_partition(seed_range, humidity_to_location_lookup, temperature_to_humidity_lookup,
                               light_to_temperature_lookup, water_to_light_lookup,
                               fertilizer_to_water_lookup, soil_to_fertilizer_lookup, seed_to_soil_lookup):
    seed_start = seed_range[0]
    seed_range = seed_range[1]

    seed_to_location = compose(humidity_to_location_lookup.map, temperature_to_humidity_lookup.map,
                               light_to_temperature_lookup.map, water_to_light_lookup.map,
                               fertilizer_to_water_lookup.map, soil_to_fertilizer_lookup.map, seed_to_soil_lookup.map)

    print_count = 10000000
    min_seed_location = seed_to_location(seed_start)

    count = 0
    print(f"Initialized with seed_start: {seed_start} seed_range: {seed_range} min_location: {min_seed_location}")

    tic = time.perf_counter()
    for index in range(seed_range):
        seed_id = seed_start + index

        if count % print_count == 0:
            toc = time.perf_counter()
            print(
                f"Started @ seed {seed_start} currently at {seed_id} elapsed time {toc - tic:0.4f} seconds after {print_count} iterations")

        seed_location = seed_to_location(seed_id)

        if seed_location < min_seed_location:
            min_seed_location = seed_location
            print(f"New min seed location {min_seed_location}")

        count = count + 1
    print(f"*** STARTED @ {seed_start} FINISHED @ {seed_id} LAST SEED SHOULD BE {seed_start + seed_range - 1} LAST_MIN_LOCATION = {min_seed_location} ***")

def generate_lookup(map_name: str, input_data: List[str]) -> CategoryLookup:
    maps : List[CategoryMap] = [parse_category_map(map_name, map_line) for map_line in input_data]
    return CategoryLookup(maps)

if __name__ == "__main__":
    seed_fertilizer()

