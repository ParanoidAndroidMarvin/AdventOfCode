import numpy as np

import aoc_api


def get_rating(binaries, bit):
    for i in range(12):
        column = binaries[:, i]

        criteria_bit = int(not bit)
        if sum(column) >= len(binaries) / 2:
            criteria_bit = int(bit)

        filter_arr = column == criteria_bit
        binaries = binaries[filter_arr]

        if len(binaries) == 1:
            break

    return int(''.join(list(map(str, binaries[0]))), 2)


# ----------------------------------------------------------------------------------------------


def get_power(binaries):
    binaries_sum = [0] * 12

    for binary in binaries:
        binary_array = list(map(int, binary));
        binaries_sum = np.add(binaries_sum, binary_array)

    gamma_rate = list(map(lambda x: '1' if (x > len(binaries) / 2) else '0', binaries_sum))
    epsilon_rate = list(map(lambda x: '0' if (x > len(binaries) / 2) else '1', binaries_sum))
    gamma_rate = ''.join(gamma_rate)
    epsilon_rate = ''.join(epsilon_rate)

    return str(int(gamma_rate, 2) * int(epsilon_rate, 2))


def get_life_support(binaries):
    binaries = [list(map(int, list(binary))) for binary in binaries]
    binaries_oxygen = np.array(binaries)
    binaries_scrubber = np.copy(binaries_oxygen)

    oxygen = get_rating(binaries_oxygen, True)
    scrubber = get_rating(binaries_scrubber, False)

    return str(oxygen * scrubber)


def solve():
    binaries = aoc_api.fetch_input(3)
    print('Power Level: ' + get_power(binaries))
    print('Life Support Level: ' + get_life_support(binaries))
