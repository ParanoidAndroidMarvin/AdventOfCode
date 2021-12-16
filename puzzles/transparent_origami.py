import numpy

import aoc_api
import numpy as np


# ------------- Common -------------
def solve():
    puzzle_input = aoc_api.fetch_input(13)
    print('Amount of dots after one fold: ' + get_number_after_first_fold(puzzle_input))
    print('Password:')
    password = get_password(puzzle_input)
    for line in password:
        print(line)


def split_paper_and_instructions(puzzle_input):
    split_index = puzzle_input.index('')
    instructions = [instruction[11:] for instruction in puzzle_input[split_index + 1:]]

    coordinates = np.array(
        [[int(number) for number in coordinate.split(',')] for coordinate in puzzle_input[:split_index]])
    coordinates = numpy.rot90(coordinates)

    paper = np.zeros((895, 1311), dtype=int)
    paper[tuple(coordinates)] += 1

    return paper, instructions


# ------------- Part 1 -------------
def get_number_after_first_fold(puzzle_input):
    paper, instructions = split_paper_and_instructions(puzzle_input)

    for instruction in instructions:
        axis = 1 if instruction.startswith('x') else 0  # get fold axis
        index = int(instruction[2:])  # get fold index

        paper, _, to_fold = np.split(paper, [index, index + 1], axis=axis)  # split paper
        to_fold = np.flip(to_fold, axis=axis)  # fold one side
        paper = paper + to_fold
        break

    return str(np.count_nonzero(paper))


# ------------- Part 2 -------------
def get_password(puzzle_input):
    paper, instructions = split_paper_and_instructions(puzzle_input)

    for instruction in instructions:
        axis = 1 if instruction.startswith('x') else 0  # get fold axis
        index = int(instruction[2:])  # get fold index

        paper, _, to_fold = np.split(paper, [index, index + 1], axis=axis)  # split paper
        to_fold = np.flip(to_fold, axis=axis)  # mirror page to fold
        paper = paper + to_fold  # stack pages

    # convert to readable password
    paper = [['.' if number == 0 else '#' for number in line] for line in paper]
    paper = [' '.join(line) for line in paper]
    return paper
