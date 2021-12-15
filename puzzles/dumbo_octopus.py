import aoc_api

# ------------- Common -------------
total_flashes = 0


class Octopus:
    def __init__(self, energy, x, y):
        self.energy = energy
        self.x = x
        self.y = y
        self.flashed = False

    def charge(self, octopus_list):
        self.energy += 1
        if self.energy > 9:
            self.flash(octopus_list)

    def flash(self, octopus_list):
        if not self.flashed:
            global total_flashes
            total_flashes += 1
            self.flashed = True
            self.charge_neighbors(octopus_list)

    def charge_neighbors(self, octopus_list):
        x = self.x
        y = self.y
        [[octopus_list[x][y].charge(octopus_list) for y in range(y - 1, y + 2) if 0 <= y <= 9] for x in range(x - 1, x + 2)
         if 0 <= x <= 9]

    def reset(self):
        if self.flashed:
            self.energy = 0
            self.flashed = False


def solve():
    puzzle_input = aoc_api.fetch_input(11)
    print("The Dumbo Octopuses flashed a total of: " + count_total_flashes(puzzle_input))
    print("The Dumbo Octopuses flash all at once in step: " + all_flash(puzzle_input))


def format_input(puzzle_input):
    return [[Octopus(int(charge), x, y) for y, charge in enumerate(line)] for x, line in enumerate(puzzle_input)]


# ------------- Part 1 -------------
def count_total_flashes(puzzle_input):
    global total_flashes
    total_flashes = 0
    octopuses = format_input(puzzle_input)

    for step in range(100):
        [octopus.charge(octopuses) for octopus_line in octopuses for octopus in octopus_line]
        [octopus.reset() for octopus_line in octopuses for octopus in octopus_line]

    return str(total_flashes)


# ------------- Part 2 -------------
def all_flash(puzzle_input):
    global total_flashes
    total_flashes = 0
    step = 0

    octopuses = format_input(puzzle_input)

    while True:
        step += 1
        previous_total_flashes = total_flashes
        [octopus.charge(octopuses) for octopus_line in octopuses for octopus in octopus_line]
        [octopus.reset() for octopus_line in octopuses for octopus in octopus_line]
        if total_flashes - previous_total_flashes == 100:
            break

    return str(step)

