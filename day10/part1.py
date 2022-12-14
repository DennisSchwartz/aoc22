
class Processor:
    registers = {}
    cycle = 0
    checkpoints = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    ss_sum = 0

    def __init__(self, registers):
        self.registers = registers

    def pre_tick(self):
        pass

    def post_tick(self):
        if self.cycle in self.checkpoints:
            self.signal_strength = self.registers['x'] * self.cycle
            self.ss_sum += self.signal_strength

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

    return proc.ss_sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        res = main(f)
        print(res)
