import aoc_api


class Position:
    horizontal = 0
    depth = 0
    aim = 0

    def result(self):
        return self.horizontal * self.depth


def get_position_part1(commands):
    position = Position()
    for command in commands:
        direction, amount = command.split(' ')
        amount = int(amount)
        match direction:
            case 'forward':
                position.horizontal += amount
            case 'up':
                position.depth -= amount
            case 'down':
                position.depth += amount
    return str(position.result())


def get_position_part2(commands):
    position = Position()
    for command in commands:
        direction, amount = command.split(' ')
        amount = int(amount)
        match direction:
            case 'forward':
                position.horizontal += amount
                position.depth += amount * position.aim
            case 'up':
                position.aim -= amount
            case 'down':
                position.aim += amount
    return str(position.result())


def solve():
    commands = aoc_api.fetch_input(2)
    print('Initially calculated position: ' + get_position_part1(commands))
    print('Second calculated position: ' + get_position_part2(commands))
