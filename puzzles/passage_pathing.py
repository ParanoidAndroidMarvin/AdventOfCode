from collections import defaultdict

import aoc_api

# ------------- Common -------------
cave_map = {}


def solve():
    puzzle_input = aoc_api.fetch_input(12)
    example = ['start-A',
               'start-b',
               'A-c',
               'A-b',
               'b-d',
               'A-end',
               'b-end']
    print("Amount of possible paths: " + get_possible_paths(example))
    print("Amount of possible paths with extended time: " + get_possible_paths_extended(puzzle_input))


def map_possibilities(puzzle_input):
    global cave_map
    cave_map = defaultdict(list)
    for line in puzzle_input:
        a, b = line.strip().split('-')
        cave_map[a].append(b)
        cave_map[b].append(a)


# ------------- Part 1 -------------
def get_possible_paths(puzzle_input):
    map_possibilities(puzzle_input)
    paths = get_paths_recursively([], 'start')
    return str(len(paths))


def get_paths_recursively(current_path, next_cave):
    possible_paths = []
    current_path = current_path + [next_cave]
    if next_cave == "end":
        return [current_path]
    for cave in cave_map[next_cave]:
        if cave.isupper() or cave not in current_path:
            possible_paths = possible_paths + get_paths_recursively(current_path, cave)
    return possible_paths


# ------------- Part 2 -------------
def get_possible_paths_extended(puzzle_input):
    map_possibilities(puzzle_input)
    paths = get_paths_recursively_extended([], 'start')
    return str(len(paths))


def get_paths_recursively_extended(current_path, next_cave):
    possible_paths = []
    current_path = current_path + [next_cave]
    visited_twice = check_cave_visited_twice(current_path)

    if next_cave == "end":
        return [current_path]
    for cave in cave_map[next_cave]:
        if cave.isupper() or (current_path.count(cave) < 1 if visited_twice else 2 and not cave == 'start'):
            possible_paths = possible_paths + get_paths_recursively_extended(current_path, cave)
    return possible_paths


def check_cave_visited_twice(current_path):
    visited = set()
    for cave in current_path:
        if cave.islower() and cave in visited:
            return True
        visited.add(cave)
    return False
