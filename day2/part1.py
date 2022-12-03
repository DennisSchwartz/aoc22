
SCORE_MAP = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

WINNERS = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}


def main(in_file):
    score = 0
    for line in in_file.readlines():
        line = line.strip()
        play, response = line.split()
        score += SCORE_MAP[response]
        if SCORE_MAP[response] == SCORE_MAP[play]:
            score += 3
        if response == WINNERS[play]:
            score += 6

    print(score)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
