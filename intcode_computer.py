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
        self.first_pass = True
        self.output = 0
        self.rel_offset = 0
        for _ in range(100000):
            program.append(0)

    def add_input(self, input):
        self.inputs.append(input)

    def get_params(self, program, param_flags):

        vals = []
        for i in range(3):
            if (self.idx + i + 1) >= len(program):
                vals.append(0)
                break
            if param_flags[i] == 0 or param_flags[i] is None:
                if i == 2:
                    vals.append(program[self.idx + 1 + i])
                else:
                    vals.append(program[program[self.idx + 1 + i]])
            elif param_flags[i] == 1:
                vals.append(program[self.idx + 1 + i])
            elif param_flags[i] == 2:
                val = program[self.idx + 1 + i] + self.rel_offset
                if i == 2:
                    vals.append(val)
                else:
                    vals.append(program[val])
        p1, p2, p3 = vals
        return p1, p2, p3

    def add_opcode(self, program, param_flags):
        # opcode 1
        p1, p2, p3 = self.get_params(program, param_flags)
        res = p1 + p2
        program[p3] = res

    def mul_opcode(self, program, param_flags):
        # opcode 2
        p1, p2, p3 = self.get_params(program, param_flags)
        res = p1 * p2
        program[p3] = res

    def input_opcode(self, program, param_flags):
        # opcode 3
        if param_flags[0] == 0 or not param_flags[0]:
            p1 = program[self.idx + 1]
        elif param_flags[0] == 1:
            p1 = self.idx + 1
        elif param_flags[0] == 2:
            p1 = program[self.idx + 1] + self.rel_offset
        if self.first_pass:
            program[p1] = self.phase
            self.first_pass = False
        else:
            program[p1] = self.inputs.popleft()

    def output_opcode(self, program, param_flags):
        # opcode 4
        p1, p2, p3 = self.get_params(program, param_flags)
        self.output = p1


    def jump_if_true_opcode(self, program, param_flags):
        # opcode 5
        p1, p2, p3 = self.get_params(program, param_flags)
        if p1 != 0:
            return p2
        else:
            return False

    def jump_if_false_opcode(self, program, param_flags):
        # opcode 6
        p1, p2, p3 = self.get_params(program, param_flags)
        if p1 == 0:
            return p2
        else:
            return False

    def less_than_opcode(self, program, param_flags):
        # opcode 7
        p1, p2, p3 = self.get_params(program, param_flags)
        res = 1 if p1 < p2 else 0
        program[p3] = res

    def equals_opcode(self, program, param_flags):
        # opcode 8
        p1, p2, p3 = self.get_params(program, param_flags)
        res = 1 if p1 == p2 else 0
        program[p3] = res

    def adj_rel_base_opcode(self, program, param_flags):
        # opcode 9
        p1, p2, p3 = self.get_params(program, param_flags)
        self.rel_offset += p1


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
                if len(self.inputs) == 0:
                    break
                self.input_opcode(self.program, param_flags)
                self.idx += 2
            elif opcode == 4:
                self.output_opcode(self.program, param_flags)
                if self.next_comp:
                    self.next_comp.add_input(self.output)
                print(self.output)
                self.idx += 2
            elif opcode == 5:
                new_idx = self.jump_if_true_opcode(self.program, param_flags)
                if new_idx is not False:
                    self.idx = new_idx
                else:
                    self.idx += 3
            elif opcode == 6:
                new_idx = self.jump_if_false_opcode(self.program, param_flags)
                if new_idx is not False:
                    self.idx = new_idx
                else:
                    self.idx += 3
            elif opcode == 7:
                self.less_than_opcode(self.program, param_flags)
                self.idx += 4
            elif opcode == 8:
                self.equals_opcode(self.program, param_flags)
                self.idx += 4
            elif opcode == 9:
                self.adj_rel_base_opcode(self.program, param_flags)
                self.idx += 2
            elif opcode == 99:
                self.halted = True
                break

        return self.output

    def __repr__(self):
        return f'Intcode_Computer({self.phase}, {self.inputs})'