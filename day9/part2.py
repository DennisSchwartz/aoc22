from typing import Tuple


def step(direction: str, pos: Tuple[int, int]) -> Tuple[int, int]:
    if direction == 'U':
        return pos[0] + 1, pos[1]
    if direction == 'D':
        return pos[0] - 1, pos[1]
    if direction == 'L':
        return pos[0], pos[1] - 1
    if direction == 'R':
        return pos[0], pos[1] + 1

    raise ValueError(f'Unexpected direction! Accepted: U, D, L, R - Received: {direction}')


def follow(head_pos: Tuple[int, int], tail_pos: Tuple[int, int]) -> Tuple[int, int]:
    v_diff = head_pos[0] - tail_pos[0]
    h_diff = head_pos[1] - tail_pos[1]
    if abs(v_diff) > 1 or abs(h_diff) > 1:
        if v_diff > 0:
            tail_pos = (tail_pos[0] + 1, tail_pos[1])
        if h_diff > 0:
            tail_pos = (tail_pos[0], tail_pos[1] + 1)
        if v_diff < 0:
            tail_pos = (tail_pos[0] - 1, tail_pos[1])
        if h_diff < 0:
            tail_pos = (tail_pos[0], tail_pos[1] - 1)
    return tail_pos


def main(in_file):
    num_of_knots = 10
    seen_tail_positions = set()
    knots = [(0, 0)] * num_of_knots
    seen_tail_positions.add(knots[-1])
    for line in in_file.readlines():
        direction, steps = line.split()
        for _ in range(int(steps)):
            knots[0] = step(direction, knots[0])
            for ki in range(1, len(knots)):
                lead = knots[ki - 1]
                second = knots[ki]
                knots[ki] = follow(lead, second)
                if second == knots[ki]:  # the last knot was not updated, we can break
                    break
            seen_tail_positions.add(knots[-1])

    return len(seen_tail_positions)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
