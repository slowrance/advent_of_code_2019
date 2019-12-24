from itertools import permutations

from intcode_computer import Intcode_Computer
from aoc_common import read_opcodes, make_digits, decode_digits

#initial = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# perms = permutations([0, 1, 2, 3, 4, 5])
def calc_signal(perms, initial):
    perms = perms
    program = [int(x) for x in initial]
    inputs = []
    complete = False

    max_signal = -1
    for perm in perms:
        amps = []
        first_pass = True
        for val in perm:
            ic = Intcode_Computer(program)
            ic.phase = val
            amps.append(ic)
        while not complete:
            if complete:
                break
            for i, amp in enumerate(amps):
                if i == 0 and first_pass:
                    amp.add_input(0)
                    first_pass = False
                out = amp.run_program()
                if amp.halted:
                    complete = True
                    break
                if i != len(amps) - 1:
                    amps[i+1].add_input(out)
                elif i == len(amps):
                    amps[0].add_input(out)
        if out > max_signal:
            max_signal = out
            max_perm = perm
    print(f'sequence: {max_perm} max_signal: {max_signal}')

def test_43210():
    initial = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    perms = permutations([0, 1, 2, 3, 4])
    calc_signal(perms, initial)

def test_54321():
    initial = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    perms = permutations([0, 1, 2, 3, 4])
    calc_signal(perms, initial)

def test_65210():
    initial = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    perms = permutations([0, 1, 2, 3, 4])
    calc_signal(perms, initial)

def actual_run():
    initial = [3,8,1001,8,10,8,105,1,0,0,21,42,51,76,101,118,199,280,361,442,99999,3,9,101,5,9,9,102,2,9,9,1001,9,4,9,102,2,9,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,1001,9,3,9,1002,9,5,9,101,3,9,9,1002,9,2,9,4,9,99,3,9,101,4,9,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,101,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99]
    perms = permutations([0, 1, 2, 3, 4])
    calc_signal(perms, initial)

def test_139629729():
    initial = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    perms = ([9,8,7,6,5],)
    calc_signal(perms, initial)

test_139629729()
