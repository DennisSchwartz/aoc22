
class Processor:
    registers = {}
    cycle = 0
    width = 40

    def __init__(self, registers):
        self.registers = registers

    def pre_tick(self):
        pass

    def post_tick(self):
        hor_pos = (self.cycle % self.width) - 1
        if hor_pos == 0:
            print()
        x = self.registers['x']
        if hor_pos in [x-1, x, x+1]:
            print('#', end='')
        else:
            print('.', end='')

    def tick(self):
        self.pre_tick()
        self.cycle += 1
        self.post_tick()

    def add(self, register, value):
        for _ in range(2):
            self.tick()
        self.registers[register] += value


def main(in_file):
    proc = Processor({'x': 1})

    for cmd in in_file.readlines():
        cmd = cmd.strip()
        if cmd.startswith('add'):
            cmd, val = cmd.split()
            cmd, target = cmd[:3], cmd[-1]
            proc.add(target, int(val))
        if cmd == 'noop':
            proc.tick()


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        main(f)
