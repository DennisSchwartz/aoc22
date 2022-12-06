
def main(in_file):
    overlapping_ranges = 0
    for line in in_file.readlines():
        line = line.strip()
        ranges = line.split(',')
        sets = []
        for r in ranges:
            start, end = r.strip().split('-')
            sets.append(set(range(int(start), int(end) + 1)))

        if sets[0].issubset(sets[1]) or sets[1].issubset(sets[0]):
            overlapping_ranges += 1

    print(overlapping_ranges)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
