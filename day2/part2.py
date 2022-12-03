
SCORE_MAP = {
    'A': 0,
    'B': 1,
    'C': 2
}

SCORES = [1, 2, 3]

OUTCOME_SCORES = {
    'X': (0, -1),
    'Y': (3, 0),
    'Z': (6, 1),
}


def main(in_file):
    score = 0
    for line in in_file.readlines():
        line = line.strip()
        play, outcome = line.split()
        os, mod = OUTCOME_SCORES[outcome]
        score += os
        score += SCORES[(SCORE_MAP[play] + mod) % 3]

    print(score)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
