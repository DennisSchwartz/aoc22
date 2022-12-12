
def check_to_border(grid, height_range, width_range, limit) -> bool:
    for y in range(*height_range):
        for x in range(*width_range):
            if grid[y][x] >= limit:
                return True
    return False


def main(in_file):
    grid = []
    for line in in_file.readlines():
        grid.append(list(line.strip()))

    height = len(grid)
    width = len(grid[0])

    invisible = []

    for i in range(height):
        for j in range(width):
            tree_height = grid[i][j]
            # if i == 0 or j == 0 or i == height or j == width:
            #     continue

            above = check_to_border(grid, (i-1, -1, -1), (j, j+1), tree_height)
            below = check_to_border(grid, (i+1, height), (j, j+1), tree_height)
            left = check_to_border(grid, (i, i+1), (j-1, -1, -1), tree_height)
            right = check_to_border(grid, (i, i+1), (j+1, width), tree_height)

            if left and right and above and below:
                invisible.append((i, j))

    return height * width - len(invisible)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
