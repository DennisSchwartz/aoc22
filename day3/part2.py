
items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main(in_file):
    sum_of_priorities = 0
    group_packs = []
    for line in in_file.readlines():
        line = line.strip()
        group_packs.append(set(line))
        if len(group_packs) == 3:
            common_items = set.intersection(*group_packs)
            for item in common_items:
                sum_of_priorities += items.index(item) + 1  # account for 1-indexing in problem
            group_packs = []

    print(sum_of_priorities)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
