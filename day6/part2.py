
def main(in_file):
    stream = in_file.read()
    pos = 0
    window = []
    for ch in stream:
        pos += 1
        window = window[-3:]
        window.append(ch)
        if len(set(window)) == 4:
            return pos


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        pos = main(f)
        print(pos)
