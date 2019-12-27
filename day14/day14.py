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
    components = []
    for line in text:
        components.append(convert_line_to_Component(line))
    return components



test1_input = get_input('test1.txt')
instructions = get_instructions(test1_input)
components = get_components(test1_input)
ore_needed = 0
inventory = {component.name: 0 for component in components}
inventory['ORE'] = 0
inventory = components[2].create(1, inventory, components)

print(inventory)

