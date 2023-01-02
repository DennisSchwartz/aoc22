
def compare_pairs(left, right):
    assert isinstance(left, (list, int))
    assert isinstance(right, (list, int))

    if isinstance(left, int) and isinstance(right, int):
        return left < right

    if isinstance(left, list) and not isinstance(right, list):
        right = [right]

    if isinstance(right, list) and not isinstance(left, list):
        left = [left]

    while not (len(left) == 0 or len(right) == 0):
        li, ri = left.pop(0), right.pop(0)
        if li == ri:
            continue
        else:
            return compare_pairs(li, ri)

    return len(left) == 0


def main(in_file):
    content = in_file.read()
    pairs = content.split('\n\n')
    res = 0
    for i, pair in enumerate(pairs):
        first_str, second_str = pair.split('\n')
        first = eval(first_str)
        second = eval(second_str)
        if compare_pairs(first, second):
            res += i + 1

    return res


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
