import re
from collections import defaultdict
from typing import Dict, List, Tuple


def get_stacks(lines: List[str], stack_indices: List[int]) -> Dict[int, List[str]]:
    stacks = defaultdict(list)
    for line in lines:
        for i in stack_indices:
            chunk, line = line[:4], line[4:]
            chunk = chunk.strip()
            if chunk:
                stacks[i].insert(0, chunk[1])

    return stacks


def do_moves(stacks: Dict[int, List[str]], moves: List[Tuple[int]]) -> Dict[int, List[str]]:
    for move in moves:
        amount, src, target = move
        for _ in range(amount):
            stacks[target].append(stacks[src].pop())
    return stacks


def main(in_file):
    lines = in_file.readlines()
    stacks_raw = []
    stacks_end = False
    stack_indices = []
    moves_raw = []

    for line in lines:
        if line.startswith(' 1'):
            stack_indices = [int(i) for i in re.split(r'\s+', line.strip())]
        if line == '\n':
            stacks_raw.pop()
            stacks_end = True
            continue
        if not stacks_end:
            stacks_raw.append(line)
        else:
            moves_raw.append(line.strip())

    stacks = get_stacks(stacks_raw, stack_indices)

    moves = []
    for move in moves_raw:
        tmp = move.split()
        moves.append((int(tmp[1]), int(tmp[3]), int(tmp[5])))

    stacks = do_moves(stacks, moves)
    top = "".join([stacks[i+1][-1] for i in range(len(stacks))])
    print(top)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
