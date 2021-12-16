import collections

import aoc_api


# ------------- Common -------------
def solve():
    puzzle_input = aoc_api.fetch_input(14)
    print("Polymer value is:", get_polymer_value(puzzle_input))
    print("Larger Polymer value is:", get_polymer_value_improved(puzzle_input))


# ------------- Part 1 -------------
def get_polymer_value(puzzle_input):
    polymer = puzzle_input[0]
    templates = dict(template.split(' -> ') for template in puzzle_input[2:])
    templates = {key: key[0] + value + key[1] for key, value in templates.items()}

    for _ in range(10):
        polymer_pairs = [polymer[i:i + 2] for i in range(len(polymer) - 1)]
        polymer_pairs[:] = [templates[pair][:2] if pair in templates else pair[0] for pair in polymer_pairs]
        # add last character again which gets lost in previous step (to avoid complex logic in list comprehension)
        polymer = ''.join(polymer_pairs) + polymer[-1]

    element_occurrences = collections.Counter(polymer).most_common()
    return element_occurrences[0][1] - element_occurrences[-1][1]


# ------------- Part 2 -------------
def get_polymer_value_improved(puzzle_input):
    polymer = puzzle_input[0]

    # map polymer pairs in dictionary
    templates = dict(template.split(' -> ') for template in puzzle_input[2:])
    templates = {key: (key[0] + value, value + key[1]) for key, value in templates.items()}

    # initialize element pair counter
    element_pairs = collections.defaultdict(int)
    for i in range(len(polymer) - 1):
        element_pairs[polymer[i:i + 2]] += 1

    element_count = collections.defaultdict(int, collections.Counter(polymer).most_common())

    # simulate polymer growth
    for _ in range(40):
        element_pairs_tmp = collections.defaultdict(int)
        for key, value in element_pairs.items():
            element_pairs_tmp[templates[key][0]] += value
            element_pairs_tmp[templates[key][1]] += value
            element_count[templates[key][0][1]] += value
        element_pairs = element_pairs_tmp

    # get most and least common element
    element_count = dict(sorted(element_count.items(), key=lambda item: item[1]))
    element_count = list(element_count.values())
    return element_count[-1] - element_count[0]
