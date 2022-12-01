
def main(in_file):
    elves = []
    curr_elf = []
    max_cals = 0
    for line in in_file.readlines():
        line = line.strip()
        if line == '':
            cur_sum = sum(curr_elf)
            elves.append(cur_sum)
            if cur_sum > max_cals:
                max_cals = cur_sum
            curr_elf = []
        else:
            cal = int(line)
            curr_elf.append(cal)

    print(f'Max calories for elf: {max_cals}')
    print(f'Max calories for top three elves: {sum(sorted(elves)[-3:])}')


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
