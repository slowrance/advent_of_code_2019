from aoc_common import read_opcodes, make_digits, decode_digits

initial = read_opcodes('day05_input.txt')


def initialize():
    program = initial.copy()
    # for idx in program:
    #     program[idx] = int(program[idx])
    return [int(x) for x in program]

def get_params(idx, program, param_flags):
    p1 = program[idx + 1] if param_flags[0] else program[program[idx + 1]]
    p2 = program[idx + 2] if param_flags[1] else program[program[idx + 2]]
    p3 = program[idx + 3] if param_flags[2] else program[program[idx + 3]]
    return p1, p2, p3

def add_opcode(idx, program, param_flags):
    p1, p2, p3 = get_params(idx, program, param_flags)
    # program[program[idx + 3]] = program[program[idx + 1]] + program[program[idx + 2]]
    p3 = p1 + p2
    program[program[idx + 3]] = p3


def mul_opcode(idx, program, param_flags):
    p1, p2, p3 = get_params(idx, program, param_flags)
    # program[program[idx + 3]] = program[program[idx + 1]] * program[program[idx + 2]]
    p3 = p1 * p2
    program[program[idx + 3]] = p3


def input_opcode(idx, program):
    program[program[idx + 1]] = 1


def output_opcode(idx, program):
    print(program[program[idx + 1]])


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
            output_opcode(idx, program)
            idx += 2
        elif opcode == 99:
            break

    return program[0], program[1], program[2]


if __name__ == '__main__':
    program = initialize()
    run_program(program)
