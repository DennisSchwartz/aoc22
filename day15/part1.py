import re
from collections import defaultdict

import numpy as np


def show_map(sensors, beacons):
    combined = sensors.union(beacons)
    min_x, max_x, max_y = np.inf, 0, 0
    for p in combined:
        x, y = p
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    for y in range(0, max_y + 2):
        for x in range(min_x - 2, max_x + 2):
            p = (x, y)
            symbol = '.'
            if p in sensors:
                symbol = 'S'
            if p in beacons:
                symbol = 'B'
            print(symbol, end='')

        print()

    print()


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main(in_file):
    sensors = set()
    beacons = set()
    combos = {}
    for line in in_file.readlines():
        pos = [int(m[1]) for m in re.findall(r'(x=|y=)(-*\d+)', line)]
        sensor_pos = tuple(pos[:2])
        beacon_pos = tuple(pos[2:])
        sensors.add(sensor_pos)
        beacons.add(beacon_pos)
        combos[sensor_pos] = beacon_pos

    # show_map(sensors, beacons)

    covered_in_line = defaultdict(set)

    for a, b in combos.items():
        dist = manhattan_distance(a, b)
        starting_line = a[1]
        starting_col = a[0]
        covered = list(range(starting_col - dist, starting_col + dist))
        covered_in_line[starting_line].update(set(covered))
        for dist in range(1, dist):
            covered = covered[1:-1]
            up = starting_line - dist
            down = starting_line + dist
            covered_in_line[up] = set(covered)
            covered_in_line[down] = set(covered)



    # return len(covered_in_line[2000000])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
