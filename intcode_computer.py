from collections import deque

from aoc_common import read_opcodes, make_digits, decode_digits

class Intcode_Computer():

    def __init__(self, program):
        self.program = program
        self.inputs = deque()
        self.phase = -1
        self.halted = False
        self.idx = 0
        self.next_comp = None

    def add_input(self, input):
        self.inputs.append(input)

    def get_two_params(self, program, param_flags):
        p1 = program[self.idx + 1] if param_flags[0] else program[program[self.idx + 1]]
        p2 = program[self.idx + 2] if param_flags[1] else program[program[self.idx + 2]]
        return p1, p2

    def get_one_param(self, program, param_flags):
        p1 = program[self.idx + 1] if param_flags[0] else program[program[self.idx + 1]]
        return p1

    def add_opcode(self, program, param_flags):
        p1, p2 = self.get_two_params(program, param_flags)
        p3 = p1 + p2
        program[program[self.idx + 3]] = p3

    def mul_opcode(self, program, param_flags):
        p1, p2 = self.get_two_params(program, param_flags)
        # program[program[idx + 3]] = program[program[idx + 1]] * program[program[idx + 2]]
        p3 = p1 * p2
        program[program[self.idx + 3]] = p3

    def input_opcode(self, program):
        if self.idx == 0:
            program[program[self.idx + 1]] = self.phase
        else:
            program[program[self.idx + 1]] = self.inputs.popleft()

    def output_opcode(self, program, param_flags):
        p1 = self.get_one_param(program, param_flags)
        self.output = p1
        # self.next_comp.add_input(self.output)
        # self.next_comp.run_program()

    def jump_if_true_opcode(self, program, param_flags):
        p1, p2 = self.get_two_params(program, param_flags)
        if p1 != 0:
            return p2
        else:
            return False

    def jump_if_false_opcode(self, program, param_flags):
        p1, p2 = self.get_two_params(program, param_flags)
        if p1 == 0:
            return p2
        else:
            return False

    def less_than_opcode(self, program, param_flags):
        p1, p2 = self.get_two_params(program, param_flags)
        p3 = 1 if p1 < p2 else 0
        program[program[self.idx + 3]] = p3

    def equals_opcode(self, program, param_flags):
        p1, p2 = self.get_two_params(program, param_flags)
        p3 = 1 if p1 == p2 else 0
        program[program[self.idx + 3]] = p3

    def run_program(self):
        while self.idx < len(self.program):
            opcode, param_flags = decode_digits(make_digits(self.program[self.idx]))
            if opcode == 1:
                self.add_opcode(self.program, param_flags)
                self.idx += 4
            elif opcode == 2:
                self.mul_opcode(self.program, param_flags)
                self.idx += 4
            elif opcode == 3:
                self.input_opcode(self.program)
                self.idx += 2
            elif opcode == 4:
                self.output_opcode(self.program, param_flags)
                self.next_comp.add_input(self.output)
                self.idx += 2
            elif opcode == 5:
                new_idx = self.jump_if_true_opcode(self.program, param_flags)
                if new_idx:
                    self.idx = new_idx
                else:
                    self.idx += 3
            elif opcode == 6:
                new_idx = self.jump_if_false_opcode(self.program, param_flags)
                if new_idx:
                    self.idx = new_idx
                else:
                    self.idx += 3
            elif opcode == 7:
                self.less_than_opcode(self.program, param_flags)
                self.idx += 4
            elif opcode == 8:
                self.equals_opcode(self.program, param_flags)
                self.idx += 4
            elif opcode == 99:
                self.halted = True
                break

        return self.output

    def __repr__(self):
        return f'Intcode_Computer({self.inputs})'