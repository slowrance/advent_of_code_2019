from aoc_common import read_opcodes


initial = read_opcodes( 'day05_input.txt')


def initialize():
    program = initial.copy()
    program[1] = 1
    return program

def add_opcode(idx, program):
    program[program[idx + 3]] = program[program[idx + 1]] + program[program[idx + 2]]

def mul_opcode(idx, program):
    program[program[idx + 3]] = program[program[idx + 1]] * program[program[idx + 2]]

def input_opcode(idx, program):
    pass

def output_opcode(idx, program):
    print(program[idx + 1])




def run_program(program):
    idx = 0
    while idx < len(program):
        if program[idx] == 1:
            add_opcode(idx, program)
        elif program[idx] == 2:
            mul_opcode(idx, program)
        elif program[idx] == 99:
            break
        idx += 4

    return program[0], program[1], program[2]

if __name__ == '__main__':
    program = initialize()
    run_program(program)


