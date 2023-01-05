import numpy as np

SAND_START_POS = (500, 0)


def show_cave(solid_points, sand):
    combined = solid_points.union(sand)
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
            if p in solid_points:
                symbol = '#'
            if p in sand:
                symbol = 'o'
            if p == SAND_START_POS:
                symbol = '+'
            print(symbol, end='')

        print()

    print()


def process_sand(rock, sand):
    lowest_rock_pos = max([r[1] for r in rock])
    solid_points = rock.union(sand)
    sand_pos = SAND_START_POS
    at_rest = False
    while not at_rest:
        # check if falling
        if sand_pos[1] > lowest_rock_pos:
            return rock, sand, True
        # check down
        elif not (sand_pos[0], sand_pos[1] + 1) in solid_points:
            sand_pos = (sand_pos[0], sand_pos[1] + 1)
            continue
        # check down + left
        elif not (sand_pos[0]-1, sand_pos[1] + 1) in solid_points:
            sand_pos = (sand_pos[0]-1, sand_pos[1] + 1)
            continue
        # check down + right
        elif not (sand_pos[0]+1, sand_pos[1] + 1) in solid_points:
            sand_pos = (sand_pos[0]+1, sand_pos[1] + 1)
            continue
        else:
            at_rest = True

    sand.add(sand_pos)
    return rock, sand, False


def main(in_file):
    rock = set()
    sand = set()
    max_x = 0
    max_y = 0
    for line in in_file.readlines():
        line = line.strip()
        points = []
        for point in line.split(' -> '):
            points.append(tuple(int(p) for p in point.split(',')))

        start = points.pop(0)
        while True:
            end = points.pop(0)
            a, b = sorted([start[0], end[0]])
            for x in range(a, b + 1):
                if x > max_x:
                    max_x = x
                c, d = sorted([start[1], end[1]])
                for y in range(c, d + 1):
                    rock.add((x, y))
                    if y > max_y:
                        max_y = y
            if len(points) < 1:
                break
            start = end

    show_cave(rock, sand)

    falling = False
    while not falling:
        rock, sand, falling = process_sand(rock, sand)

    show_cave(rock, sand)

    return len(sand)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
