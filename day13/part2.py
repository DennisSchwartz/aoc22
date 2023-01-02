from copy import deepcopy
from part1 import compare_pairs


def main(in_file):
    content = []
    for line in in_file.readlines():
        line = line.strip()
        if not line:
            continue
        content.append(eval(line))

    divider_packets = [[[2]], [[6]]]
    content = content + divider_packets

    for i in range(len(content)):
        for j in range(i + 1, len(content)):
            left, right = deepcopy(content[i]), deepcopy(content[j])
            correct = compare_pairs(left, right)
            if not correct:
                content[i], content[j] = content[j], content[i]

    return (content.index(divider_packets[0]) + 1) * (content.index(divider_packets[1]) + 1)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
