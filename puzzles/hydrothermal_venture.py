import aoc_api


# ------------ classes --------------
class Coordinate:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    @classmethod
    def from_string(cls, string):
        (x, y) = string.split(',')
        return cls(x, y)


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @classmethod
    def from_string(cls, string):
        (start, end) = string.split(' -> ')
        return cls(Coordinate.from_string(start), Coordinate.from_string(end))

    def is_horizontal(self):
        return self.start.x == self.end.x

    def is_vertical(self):
        return self.start.y == self.end.y

    def get_coordinates(self, include_diagonal):
        start = self.start
        end = self.end

        if self.is_horizontal():
            direction = 1 if start.y < end.y else -1
            return [Coordinate(start.x, y) for y in range(start.y, end.y + direction, direction)]
        if self.is_vertical():
            direction = 1 if start.x < end.x else -1
            return [Coordinate(x, start.y) for x in range(start.x, end.x + direction, direction)]
        if include_diagonal:
            direction_x = 1 if start.x < end.x else -1
            direction_y = 1 if start.y < end.y else -1
            range_x = range(start.x, end.x + direction_x, direction_x)
            range_y = range(start.y, end.y + direction_y, direction_y)

            return [Coordinate(x, y) for [x, y] in [[range_x[i], range_y[i]] for i in range(len(range_x))]]


# ------------ transform input --------------
def get_coordinates(puzzle_input):
    return list(map(lambda x: Line.from_string(x), puzzle_input))


# ------------ generate map --------------
def plot_map(vent_map, vent_coordinates):
    for coordinate in vent_coordinates:
        vent_map[coordinate.x][coordinate.y] += 1


def count_overlaps(vent_map):
    values = [vent for line in vent_map for vent in line]
    return sum(value >= 2 for value in values)


# ---------------------------------------------------------------------------------------------------------------------


def get_vent_map_simple(vents):
    vent_map = [[0] * 1000 for _ in range(1000)]
    vent_coordinates = []

    for vent in vents:
        coordinates = vent.get_coordinates(False)
        if coordinates is not None:
            vent_coordinates.extend(coordinates)
    plot_map(vent_map, vent_coordinates)

    return str(count_overlaps(vent_map))


def get_vent_map_complete(vents):
    vent_map = [[0] * 1000 for _ in range(1000)]
    vent_coordinates = []

    for vent in vents:
        coordinates = vent.get_coordinates(True)
        if coordinates is not None:
            vent_coordinates.extend(coordinates)
    plot_map(vent_map, vent_coordinates)

    return str(count_overlaps(vent_map))


def solve():
    puzzle_input = aoc_api.fetch_input(5)
    vents = get_coordinates(puzzle_input)

    print('Amount of overlapping vents (simple):' + get_vent_map_simple(vents))
    print('Amount of overlapping vents (complete):' + get_vent_map_complete(vents))
