from functools import reduce

import aoc_api


# ------------- Part 1 -------------
def get_point_risk_level(puzzle_input):
    height_map = get_height_map(puzzle_input)
    risk_levels = []

    for x in range(len(height_map)):
        for y in range(len(height_map[0])):
            height = height_map[x][y]
            adjacent_heights = get_neighbours(height_map, x, y)
            if all(height < adjacent_height for adjacent_height in adjacent_heights):
                risk_levels.append(height + 1)

    return str(sum(risk_levels))


def get_height_map(puzzle_input):
    return [[int(element) for element in line] for line in puzzle_input]


def get_neighbours(height_map, x, y):
    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    return [height_map[x + dx][y + dy] if 0 <= (x + dx) < len(height_map) and 0 <= (y + dy) < len(height_map[0]) else 9
            for dx, dy in directions]


# ------------- Part 2 -------------
class Point:
    def __init__(self, height, mapped):
        self.height = height
        self.mapped = mapped


def get_basin_risk_level(puzzle_input):
    height_map = get_improved_height_map(puzzle_input)
    basin_sizes = []

    for x in range(len(height_map)):
        for y in range(len(height_map[0])):
            point = height_map[x][y]
            if point.height < 9 and not point.mapped:
                basin_sizes.append(map_basin_recursive(height_map, x, y))

    largest_basins = sorted(basin_sizes, reverse=True)[:3]
    return str(reduce(lambda a, b: a * b, largest_basins))


def get_improved_height_map(puzzle_input):
    return [[Point(int(element), False) for element in line] for line in puzzle_input]


def map_basin_recursive(height_map, x, y):
    if not 0 <= x < len(height_map) or not 0 <= y < len(height_map[0]):
        return 0
    point = height_map[x][y]
    if point.height == 9 or point.mapped:
        return 0

    size = 1
    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    point.mapped = True
    for dx, dy in directions:
        size += map_basin_recursive(height_map, x + dx, y + dy)
    return size


# ------------- Common -------------

def solve():
    puzzle_input = aoc_api.fetch_input(9)
    print('Risk level of low points: ' + get_point_risk_level(puzzle_input))
    print('Risk level of basins: ' + get_basin_risk_level(puzzle_input))
