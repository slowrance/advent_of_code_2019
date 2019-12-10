

def read_opcodes(filename):
    opcodes = []
    with open(filename) as f:
        opcodes += f.read().split(',')
    return opcodes

def make_digits(num):
    digits = [x for x in str(num)]
    for idx, digit in enumerate(digits):
        if digit == '-':
            digits[idx] = 0
            digits[idx + 1] = int(digits[idx + 1]) * -1
    return digits

def decode_digits(digits):
    p1 = None
    p2 = None
    p3 = None
    opcode = int(''.join(digits[-2:]))
    if len(digits) > 2:
        p1 = int(digits[-3])
    if len(digits) > 3:
        p2 = int(digits[-4])
    if len(digits) > 4:
        p3 = int(digits[-5])

    return (opcode, (p1, p2, p3))
