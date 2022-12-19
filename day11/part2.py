import re
from typing import Callable, List


class Monkey:
    items: List[int] = []
    operation: Callable[[int], int] = None
    test_divisor: int = None
    yes_monkey: int
    no_monkey: int

    def __init__(self, starting_items, operation, test_divisor, yes_monkey, no_monkey):
        self.items = starting_items
        self.operation = operation
        self.test_divisor = test_divisor
        self.yes_monkey = yes_monkey
        self.no_monkey = no_monkey
        self.items_inspected = 0

    def test(self, num: int) -> bool:
        return num % self.test_divisor == 0

    def inspect_items(self, monkeys):
        while self.items:
            item = self.items.pop(0)
            new = eval(self.operation, {'old': item})
            self.items_inspected += 1
            target = monkeys[self.no_monkey]
            to_send = sum([int(i) for i in str(new)])
            if self.test(new):
                to_send = self.test_divisor
                target = monkeys[self.yes_monkey]

            target.items.append(to_send)


def create_monkey(instructions: str) -> Monkey:
    lines = instructions.split('\n')
    # this is not robust lol
    items = [int(i) for i in lines[1].split(': ')[1].split(',')]
    operation = lines[2].split(": ")[1].split('= ')[1]
    test_num = int(lines[3].split('divisible by ')[1])
    yes_monkey = int(lines[4].split('to monkey ')[1])
    no_monkey = int(lines[5].split('to monkey ')[1])
    return Monkey(
        starting_items=items,
        operation=operation,
        test_divisor=test_num,
        yes_monkey=yes_monkey,
        no_monkey=no_monkey
    )


def main(in_file):
    monkeys = []
    lines = in_file.readlines()
    current = ''
    for line in lines:
        if len(line.strip()) > 1:
            current += line
        else:
            monkeys.append(create_monkey(current))
            current = ''

    rounds = 10000
    for i in range(rounds):
        print(f'Round {i} of {rounds}', end='\r')
        if i == 20:
            print([m.items_inspected for m in monkeys])
        for m in monkeys:
            m.inspect_items(monkeys)

    inspected = list(reversed(sorted([m.items_inspected for m in monkeys])))
    monkey_business = inspected[0] * inspected[1]
    return monkey_business


if __name__ == '__main__':
    with open('example.txt', 'r') as f:
        res = main(f)
        print(res)
