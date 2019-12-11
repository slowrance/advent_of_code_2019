from aoc_common import read_opcodes, make_digits, decode_digits

initial = read_opcodes('day05_input.txt')
# initial = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

def initialize():
    program = initial.copy()
    # for idx in program:
    #     program[idx] = int(program[idx])
    return [int(x) for x in program]


def get_two_params(idx, program, param_flags):
    p1 = program[idx + 1] if param_flags[0] else program[program[idx + 1]]
    p2 = program[idx + 2] if param_flags[1] else program[program[idx + 2]]

    # p3 = program[idx + 3] if param_flags[2] else program[program[idx + 3]]
    return p1, p2

def get_one_param(idx, program, param_flags):
    p1 = program[idx + 1] if param_flags[0] else program[program[idx + 1]]

    return p1


def add_opcode(idx, program, param_flags):
    p1, p2 = get_two_params(idx, program, param_flags)
    # program[program[idx + 3]] = program[program[idx + 1]] + program[program[idx + 2]]
    p3 = p1 + p2
    program[program[idx + 3]] = p3


def mul_opcode(idx, program, param_flags):
    p1, p2 = get_two_params(idx, program, param_flags)
    # program[program[idx + 3]] = program[program[idx + 1]] * program[program[idx + 2]]
    p3 = p1 * p2
    program[program[idx + 3]] = p3


def input_opcode(idx, program):
    program[program[idx + 1]] = 5


def output_opcode(idx, program, param_flags):
    p1 = get_one_param(idx, program, param_flags)
    print(p1)


def jump_if_true_opcode(idx, program, param_flags):
    p1, p2 = get_two_params(idx, program, param_flags)
    if p1 != 0:
        return p2
    else:
        return False


def jump_if_false_opcode(idx, program, param_flags):
    p1, p2 = get_two_params(idx, program, param_flags)
    if p1 == 0:
        return p2
    else:
        return False

def less_than_opcode(idx, program, param_flags):
    p1, p2 = get_two_params(idx, program, param_flags)
    p3 = 1 if p1 < p2 else 0
    program[program[idx + 3]] = p3


def equals_opcode(idx, program, param_flags):
    p1, p2 = get_two_params(idx, program, param_flags)
    p3 = 1 if p1 == p2 else 0
    program[program[idx + 3]] = p3

def run_program(program):
    idx = 0
    while idx < len(program):
        opcode, param_flags = decode_digits(make_digits(program[idx]))
        if opcode == 1:
            add_opcode(idx, program, param_flags)
            idx += 4
        elif opcode == 2:
            mul_opcode(idx, program, param_flags)
            idx += 4
        elif opcode == 3:
            input_opcode(idx, program)
            idx += 2
        elif opcode == 4:
            output_opcode(idx, program, param_flags)
            idx += 2
        elif opcode == 5:
            new_idx = jump_if_true_opcode(idx, program, param_flags)
            if new_idx:
                idx = new_idx
            else:
                idx += 3
        elif opcode == 6:
            new_idx = jump_if_false_opcode(idx, program, param_flags)
            if new_idx:
                idx = new_idx
            else:
                idx += 3
        elif opcode == 7:
            less_than_opcode(idx, program, param_flags)
            idx += 4
        elif opcode == 8:
            equals_opcode(idx, program, param_flags)
            idx += 4
        elif opcode == 99:
            break

    return program[0], program[1], program[2]


if __name__ == '__main__':
    program = initialize()
    run_program(program)
