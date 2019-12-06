

initial = [1, 0, 0, 3
            , 1, 1, 2, 3
            , 1, 3, 4, 3
            , 1, 5, 0, 3
            , 2, 6, 1, 19
            , 1, 5, 19, 23
            , 2, 9, 23, 27
            , 1, 6, 27, 31
            , 1, 31, 9, 35
            , 2, 35, 10, 39
            , 1, 5, 39, 43
            , 2, 43, 9, 47
            , 1, 5, 47, 51
            , 1, 51, 5, 55
            , 1, 55, 9, 59
            , 2, 59, 13, 63
            , 1, 63, 9, 67
            , 1, 9, 67, 71
            , 2, 71, 10, 75
            , 1, 75, 6, 79
            , 2, 10, 79, 83
            , 1, 5, 83, 87
            , 2, 87, 10, 91
            , 1, 91, 5, 95
            , 1, 6, 95, 99
            , 2, 99, 13, 103
            , 1, 103, 6, 107
            , 1, 107, 5, 111
            , 2, 6, 111, 115
            , 1, 115, 13, 119
            , 1, 119, 2, 123
            , 1, 5, 123, 0
            , 99, 2, 0, 14, 0]
# intcodes = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19]


def add_opcode(idx, intcodes):
    intcodes[intcodes[idx + 3]] = intcodes[intcodes[idx + 1]] + intcodes[intcodes[idx + 2]]

def mul_opcode(idx, intcodes):
    intcodes[intcodes[idx + 3]] = intcodes[intcodes[idx + 1]] * intcodes[intcodes[idx + 2]]

def initialize(noun, verb):
    intcodes = initial.copy()
    intcodes[1] = noun
    intcodes[2] = verb
    return intcodes

def run_program(intcodes):
    idx = 0
    while idx < len(intcodes):
        if intcodes[idx] == 1:
            add_opcode(idx, intcodes)
        elif intcodes[idx] == 2:
            mul_opcode(idx, intcodes)
        elif intcodes[idx] == 99:
            break
        idx += 4

    return intcodes[0], intcodes[1], intcodes[2]

def part1():
    intcodes = initialize(12, 2)
    print(run_program(intcodes))


    # part 1 337042 is too low
    # part 1 3101844 is correct

def part2():
    for noun in range(100):
        for verb in range(100):
            intcodes = initialize(noun, verb)
            result = run_program(intcodes)
            if result[0] == 19690720:
                print(result)
    # 8478 is correct answer

part2()
