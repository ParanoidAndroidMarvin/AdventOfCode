import aoc_api


# ------------- Common -------------
def solve():
    puzzle_input = aoc_api.fetch_input(8)
    print("Amount of 1, 4, 7, 8 in outputs: " + count_unique_digits(puzzle_input))
    print("Sum of outputs: " + get_output_sum(puzzle_input))


# ------------- Part 1 -------------
def count_unique_digits(puzzle_input):
    digits = get_output(puzzle_input)
    digits = [digit for line in digits for digit in line]
    return str(sum([len(digit) in [2, 3, 4, 7] for digit in digits]))


def get_output(puzzle_input):
    return [digits.split(' | ')[1].split(' ') for digits in puzzle_input]


# ------------- Part 2 -------------
def get_output_sum(puzzle_input):
    digits = format_puzzle_input(puzzle_input)
    output_numbers = []

    for inputs, outputs in digits:
        digit_map = get_digit_map(inputs)
        output_numbers.append(map_output(outputs, digit_map))

    return str(sum(output_numbers))


def map_output(outputs, digit_map):
    outputs[:] = [digit_map[''.join(sorted(output))] for output in outputs]
    return int(''.join(outputs))


def format_puzzle_input(puzzle_input):
    digits = []
    for line in puzzle_input:
        (inputs, outputs) = line.split(' | ')
        digits.append((inputs.split(' '), outputs.split(' ')))
    return digits


def get_digit_map(inputs):
    digit_map = {}
    map_elementary_digits(digit_map, inputs)
    map_non_elementary_digits(digit_map, inputs)

    # switch segments and digit + order segments
    return {''.join(sorted(v)): str(k) for k, v in digit_map.items()}


def map_elementary_digits(digit_map, inputs):
    for digit in inputs:
        match len(digit):
            case 2:
                digit_map['1'] = digit
            case 3:
                digit_map['7'] = digit
            case 4:
                digit_map['4'] = digit
            case 7:
                digit_map['8'] = digit


def map_non_elementary_digits(digit_map, inputs):
    for digit in inputs:
        if len(digit) == 6:
            if not active_elements_match(digit, digit_map['1']):
                digit_map['6'] = digit
            elif not active_elements_match(digit, digit_map['4']):
                digit_map['0'] = digit
            else:
                digit_map['9'] = digit
        if len(digit) == 5:
            if active_elements_match(digit, digit_map['1']):
                digit_map['3'] = digit
            elif sum(c in digit for c in digit_map['4']) == 3:
                digit_map['5'] = digit
            else:
                digit_map['2'] = digit


def active_elements_match(unknown_digit, known_digit):
    return all(c in unknown_digit for c in known_digit)
