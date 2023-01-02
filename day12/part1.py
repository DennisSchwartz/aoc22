import numpy as np

ELEVATION = 'abcdefghijklmnopqrstuvwxyz'


# def reconstruct_path(came_from, current):
#     return 0


def check_step(current, next_step, grid):
    current_elevation = grid[current[0]][current[1]]
    if next_step[0] < 0 or next_step[0] > (len(grid) - 1) or next_step[1] < 0 or next_step[1] > (len(grid[0]) - 1):
        next_elevation = np.inf
    else:
        next_elevation = grid[next_step[0]][next_step[1]]
    if next_elevation - current_elevation < 2:
        return 1
    else:
        return np.inf


def a_star(start, goal, h):
    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: 0}

    while open_set:
        current = next(iter(open_set))
        for pos in open_set:
            if f_score.get(pos, np.inf) < f_score[current]:
                current = pos

        if current == goal:
            # return reconstruct_path(came_from, current)
            return g_score[current]

        open_set.remove(current)
        neighbors = [
            (current[0] - 1, current[1]),  # left
            (current[0] + 1, current[1]),  # right
            (current[0], current[1] - 1),  # above
            (current[0], current[1] + 1)  # below
        ]
        for n in neighbors:
            tentative_g_score = g_score[current] + check_step(current, n, h)
            if tentative_g_score < g_score.get(n, np.inf):
                came_from[n] = current
                g_score[n] = tentative_g_score
                f_score[n] = f_score[current] + 1
                if n not in open_set:
                    open_set.add(n)

    raise Exception('Did not find a path!')


def main(in_file):
    height_map = []
    start = None
    goal = None
    for line in in_file.readlines():
        line = line.strip()
        if 'S' in line:
            start = (len(height_map), line.index('S'))
            line = line.replace('S', 'a')
        if 'E' in line:
            goal = (len(height_map), line.index('E'))
            line = line.replace('E', 'z')
        height_map.append([ELEVATION.index(l) for l in line])

    return a_star(start, goal, height_map)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
