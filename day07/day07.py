from itertools import permutations

from intcode_computer import Intcode_Computer
from aoc_common import read_opcodes, make_digits, decode_digits

initial = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# perms = permutations([0, 1, 2, 3, 4, 5])
perms = [(1, 0, 4, 3, 2)]
program = [int(x) for x in initial]
inputs = []
amps = []
for perm in perms:
    for val in perm:
        ic = Intcode_Computer(program)
        ic.add_input(val)
        amps.append(ic)
    for i, amp in enumerate(amps):
        if i == 0:
            amp.add_input(0)
        out = amp.run_program()
        if i != len(amps) - 1:
            amps[i+1].add_input(out)
        print(out)


