import statistics

import aoc_api

OPENING_BRACKETS = '([{<'
CLOSING_BRACKETS = ')]}>'
CLOSING_BRACKETS_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<':  '>'
}
ERROR_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
AUTOCOMPLETE_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


# ------------- Part 1 -------------
def get_error_score(puzzle_input):
    error_sum = 0
    for line in puzzle_input:
        error = get_error_symbol(line)
        if error is not None:
            error_sum += ERROR_SCORES[error]
    return str(error_sum)


# ------------- Part 2 -------------
def get_autocomplete_score(puzzle_input):
    autocomplete_scores = []
    filtered_puzzle_input = list(filter(lambda x: get_error_symbol(x) is None, puzzle_input))
    for line in filtered_puzzle_input:
        autocomplete_symbols = get_autocomplete_symbols(line)
        autocomplete_scores.append(calculate_score(autocomplete_symbols))
    return str(round(statistics.median(autocomplete_scores)))


def calculate_score(autocomplete_symbols):
    autocomplete_score = 0
    for symbol in autocomplete_symbols:
        autocomplete_score *= 5
        autocomplete_score += AUTOCOMPLETE_SCORES[symbol]
    return autocomplete_score


def get_autocomplete_symbols(line):
    missing_brackets = []
    for current_char in line:
        if current_char in OPENING_BRACKETS:
            missing_brackets.append(CLOSING_BRACKETS_MAP[current_char])
        else:
            missing_brackets.pop()
    return reversed(missing_brackets)


# ------------- Common -------------
def solve():
    puzzle_input = aoc_api.fetch_input(10)
    print('Error score: ' + get_error_score(puzzle_input))
    print('Autocomplete score: ' + get_autocomplete_score(puzzle_input))


def get_error_symbol(line):
    open_chunks = []
    for current_char in line:
        if current_char in OPENING_BRACKETS:
            open_chunks.append(current_char)
        else:
            opening_bracket = open_chunks.pop()
            if current_char != CLOSING_BRACKETS_MAP[opening_bracket]:
                return current_char
