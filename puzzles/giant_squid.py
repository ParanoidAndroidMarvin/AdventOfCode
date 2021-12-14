import re

import aoc_api

x = 5
y = 5


# ------------ transform input --------------
def get_numbers(puzzle_input):
    return puzzle_input[0].split(',')


def get_boards(puzzle_input):
    return [[re.split('[ ]+', puzzle_input[i + j].strip()) for j in range(y)] for i in range(2, len(puzzle_input), 6)]


# ------------ check boards --------------
def row_complete(board, numbers):
    return any([all([board[i][j] in numbers for j in range(x)]) for i in range(y)])


def column_complete(board, numbers):
    return any([all([board[j][i] in numbers for j in range(y)]) for i in range(x)])


def board_complete(board, numbers):
    return row_complete(board, numbers) or column_complete(board, numbers)


# ------------ calculate result --------------
def calculate_result(board, numbers):
    drawn_numbers = list(map(int, numbers))
    numbers_on_board = flatten_board(board)
    unmarked_numbers_on_board = filter(lambda number: number not in drawn_numbers, numbers_on_board)
    last_drawn_number = drawn_numbers[-1]
    return str(sum(unmarked_numbers_on_board) * last_drawn_number)


def flatten_board(board):
    return [int(item) for row in board for item in row]


# ---------------------------------------------------------------------------------------------------------------------


def get_winner(puzzle_input):
    numbers = get_numbers(puzzle_input)
    boards = get_boards(puzzle_input)

    # Draw the given numbers one by one
    for i in range(0, len(numbers)):
        drawn_numbers = numbers[0:i + 1]
        # Check if there is already a winner
        for j in range(len(boards)):
            if board_complete(boards[j], drawn_numbers):
                return calculate_result(boards[j], drawn_numbers)


def get_loser(puzzle_input):
    numbers = get_numbers(puzzle_input)
    boards = get_boards(puzzle_input)

    # Go through drawn numbers backwards
    for i in range(len(numbers), 0, -1):
        drawn_numbers = numbers[0:i + 1]
        # Check if one board did NOT win
        for j in range(len(boards)):
            if not board_complete(boards[j], drawn_numbers[0:-1]):
                return calculate_result(boards[j], drawn_numbers)


def solve():
    puzzle_input = aoc_api.fetch_input(4)
    print("Bingo winner is: " + get_winner(puzzle_input))
    print("Bingo loser is: " + get_loser(puzzle_input))
