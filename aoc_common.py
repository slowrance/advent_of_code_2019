

def read_opcodes(filename):
    opcodes = []
    with open(filename) as f:
        opcodes += f.read().split(',')
    return opcodes
