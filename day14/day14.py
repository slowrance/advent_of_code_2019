from Component import Component

def get_input(filename):
    with open(filename) as f:
        return f.read().splitlines()

def convert_line_to_dict(line):
    output_dict = {}
    inputs, output = line.split('=>')
    components = inputs.split(',')
    output = output.strip().split(' ')
    output_dict[output[1]] = {'qty': int(output[0])}
    comp_list = {component.strip().split(' ')[1]: component.strip().split(' ')[0] for component in components}

    output_dict[output[1]]['components'] = comp_list
    return output_dict

def convert_line_to_Component(line):
    output_dict = {}
    inputs, output = line.split('=>')
    components = inputs.split(',')
    output = output.strip().split(' ')
    component = Component(output[1])
    component.out_qty = int(output[0])
    comp_list = {component.strip().split(' ')[1]: int(component.strip().split(' ')[0]) for component in components}
    component.inputs = comp_list
    return component



def get_instructions(text):
    instructions = []
    for line in text:
        instructions.append(convert_line_to_dict(line))
    return instructions

def get_components(text):
    components = {}
    for line in text:
        component = convert_line_to_Component(line)
        components[component.name] = component
    return components

def part1(input):
    # instructions = get_instructions(input)
    components = get_components(input)
    # ore_needed = 0
    inventory = {component: 0 for component in components}
    inventory['ORE'] = 0
    inventory = components['FUEL'].create(1, inventory, components)
    print(inventory)
    return inventory

test1_input = get_input('test1.txt')
test2_input = get_input('test2.txt')

# test1_result = part1(test1_input)
# assert test1_result['ORE'] == 31

test2_result = part1(test2_input)
assert test2_result['ORE'] == 165




