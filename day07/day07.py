import copy
from itertools import permutations

from intcode_computer import Intcode_Computer
from aoc_common import read_opcodes, make_digits, decode_digits


def create_amps(perm, program):
    amps = []
    for n in range(len(perm)):
        ic = Intcode_Computer(copy.deepcopy(program))
        ic.phase = perm[n]
        amps.append(ic)
    for i, amp in enumerate(amps):
        if i == len(amps) - 1:
            amp.next_comp = amps[0]
        else:
            amp.next_comp = amps[i + 1]
    return amps

def calc_signal(perms, initial):
    perms = perms
    program = [int(x) for x in initial]
    inputs = []

    max_signal = -1
    for perm in perms:
        amps = create_amps(perm, program)
        complete = False
        while not complete:
            for i, amp in enumerate(amps):
                if i == 0 and amp.first_pass:
                    amp.add_input(0)
                out = amp.run_program()
            if amps[-1].halted:
                complete = True
                break

                # elif i == len(amps):
                #     amps[0].add_input(out)
        if amps[-1].output > max_signal:
            max_signal = amps[-1].output
            max_perm = perm
    return f'sequence: {max_perm} max_signal: {max_signal}'

def test_43210():
    initial = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    perms = permutations([0, 1, 2, 3, 4])
    return calc_signal(perms, initial)

def test_54321():
    initial = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    perms = permutations([0, 1, 2, 3, 4])
    return calc_signal(perms, initial)

def test_65210():
    initial = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    perms = permutations([0, 1, 2, 3, 4])
    ret = calc_signal(perms, initial)
    print(ret)
    return ret

def actual_run():
    initial = [3,8,1001,8,10,8,105,1,0,0,21,42,51,76,101,118,199,280,361,442,99999,3,9,101,5,9,9,102,2,9,9,1001,9,4,9,102,2,9,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,1001,9,3,9,1002,9,5,9,101,3,9,9,1002,9,2,9,4,9,99,3,9,101,4,9,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,101,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99]
    perms = permutations([0, 1, 2, 3, 4])
    ret = calc_signal(perms, initial)
    print(ret)
    return ret

def test_139629729():
    initial = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    perms = permutations([9,8,7,6,5])
    ret = calc_signal(perms, initial)
    print(ret)
    return ret

def test_18216():
    initial = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    perms = permutations([9,8,7,6,5])
    ret = calc_signal(perms, initial)
    print(ret)
    return ret

def test_part2():
    initial = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 42, 51, 76, 101, 118, 199, 280, 361, 442, 99999, 3, 9, 101, 5, 9,
               9, 102, 2, 9, 9, 1001, 9, 4, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 3, 9, 4, 9, 99, 3, 9, 1002, 9, 4,
               9, 1001, 9, 3, 9, 1002, 9, 5, 9, 101, 3, 9, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 101, 4, 9, 9, 1002, 9, 2,
               9, 1001, 9, 3, 9, 1002, 9, 3, 9, 101, 4, 9, 9, 4, 9, 99, 3, 9, 101, 3, 9, 9, 1002, 9, 3, 9, 101, 2, 9, 9,
               4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2,
               9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002,
               9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9,
               1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3,
               9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3,
               9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4,
               9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4,
               9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2,
               9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9,
               2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2,
               9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102,
               2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001,
               9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99]
    perms = permutations([9, 8, 7, 6, 5])
    ret = calc_signal(perms, initial)
    print(ret)
    return ret

# testing part 1
assert test_65210() == 'sequence: (1, 0, 4, 3, 2) max_signal: 65210'
assert test_54321() == 'sequence: (0, 1, 2, 3, 4) max_signal: 54321'
assert test_43210() == 'sequence: (4, 3, 2, 1, 0) max_signal: 43210'
assert actual_run() == 'sequence: (0, 3, 4, 2, 1) max_signal: 75228'
assert test_139629729() == 'sequence: (9, 8, 7, 6, 5) max_signal: 139629729'
assert test_18216() == 'sequence: (9, 7, 8, 5, 6) max_signal: 18216'
test_part2()

