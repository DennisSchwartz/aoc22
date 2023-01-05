import numpy as np

SAND_START_POS = (500, 0)


def show_cave(rock, sand):
    combined = rock.union(sand)
    lowest_rock_pos = max([r[1] for r in rock])
    min_x, max_x, max_y = np.inf, 0, 0
    for p in combined:
        x, y = p
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    for y in range(0, max_y + 3):
        for x in range(min_x - 2, max_x + 2):
            p = (x, y)
            symbol = '.'
            if p in rock or y == lowest_rock_pos + 2:
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
    full = False

    def check_collision(pos):
        return pos in solid_points or pos[1] == lowest_rock_pos + 2

    while not at_rest:
        # check down
        if not check_collision((sand_pos[0], sand_pos[1] + 1)):
            sand_pos = (sand_pos[0], sand_pos[1] + 1)
            continue
        # check down + left
        elif not check_collision((sand_pos[0]-1, sand_pos[1] + 1)):
            sand_pos = (sand_pos[0]-1, sand_pos[1] + 1)
            continue
        # check down + right
        elif not check_collision((sand_pos[0]+1, sand_pos[1] + 1)):
            sand_pos = (sand_pos[0]+1, sand_pos[1] + 1)
            continue
        else:
            at_rest = True

    sand.add(sand_pos)

    if sand_pos == SAND_START_POS:
        full = True

    return rock, sand, full


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
