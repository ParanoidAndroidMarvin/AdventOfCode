import aoc_api


def get_fish_map(puzzle_input):
    fishes = puzzle_input.split(',')
    return [fishes.count(str(i)) for i in range(9)]


def reduce_counter(fishes):
    spawning_fish = fishes.pop(0)
    fishes.append(0)

    fishes[8] = spawning_fish
    fishes[6] += spawning_fish


def simulate_growth_80(puzzle_input):
    fishes = get_fish_map(puzzle_input)
    for i in range(80):
        reduce_counter(fishes)
    return str(sum(fishes))


def simulate_growth_256(puzzle_input):
    fishes = get_fish_map(puzzle_input)
    for i in range(256):
        reduce_counter(fishes)
    return str(sum(fishes))


def solve():
    puzzle_input = aoc_api.fetch_input(6)[0]
    print('Amount of fish after 80 days: ' + simulate_growth_80(puzzle_input))
    print('Amount of fish after 256 days: ' + simulate_growth_256(puzzle_input))
