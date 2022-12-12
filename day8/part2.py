
def check_to_border(grid, height_range, width_range, limit) -> bool:
    score = 0
    for y in range(*height_range):
        for x in range(*width_range):
            score += 1
            if grid[y][x] >= limit:
                return score
    return score


def main(in_file):
    grid = []
    for line in in_file.readlines():
        grid.append(list(line.strip()))

    height = len(grid)
    width = len(grid[0])

    max_score = 0

    for i in range(height):
        for j in range(width):
            tree_height = grid[i][j]

            above = check_to_border(grid, (i-1, -1, -1), (j, j+1), tree_height)
            below = check_to_border(grid, (i+1, height), (j, j+1), tree_height)
            left = check_to_border(grid, (i, i+1), (j-1, -1, -1), tree_height)
            right = check_to_border(grid, (i, i+1), (j+1, width), tree_height)

            prod = left * right * above * below
            if prod > max_score:
                max_score = prod

    return max_score


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
