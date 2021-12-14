import statistics

import aoc_api


def convert_to_list(puzzle_input):
    return [int(pos) for pos in puzzle_input.split(',')]


def calculate_fuel_usage(distance):
    return int((distance * (distance + 1)) / 2)


def get_fuel_consumption(positions):
    center = statistics.median_high(positions)
    fuel_consumption = [abs(position - center) for position in positions]
    return str(sum(fuel_consumption))


def get_fuel_consumption_new_formula(positions):
    fuel_consumption = [sum([calculate_fuel_usage(abs(position - i)) for position in positions])
                        for i in range(max(positions))]
    return str(min(fuel_consumption))


def solve():
    positions = convert_to_list(aoc_api.fetch_input(7)[0])
    print('Fuel required to align crabs: ' + get_fuel_consumption(positions))
    print('Fuel required to align crabs with new fuel formula: ' + get_fuel_consumption_new_formula(positions))
