
items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main(in_file):
    sum_of_priorities = 0
    for line in in_file.readlines():
        line = line.strip()
        compartment1 = line[:len(line) // 2]
        compartment2 = line[len(line) // 2:]
        common_items = set(compartment1).intersection(set(compartment2))
        for item in common_items:
            sum_of_priorities += items.index(item) + 1  # account for 1-indexing in problem

    print(sum_of_priorities)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
