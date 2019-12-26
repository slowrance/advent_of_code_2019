import numpy as np
from collections import namedtuple
from typing import List
from functools import reduce

from Moon import Moon

# Moon = namedtuple('Moon', 'x y z')

# actual input
moon_input = '''
<x=-3, y=15, z=-11>
<x=3, y=13, z=-19>
<x=-13, y=18, z=-2>
<x=6, y=0, z=-1>'''

# # test input
# moon_input = '''
# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>'''

moons_text = moon_input.strip().splitlines()


def gcd(*numbers):
    """
    Return the greatest common divisor of 1 or more integers
    Examples
    --------
    >>> gcd(5)
    5
    >>> gcd(30, 40)
    10
    >>> gcd(120, 40, 60)
    20
    """
    # Am I terrible for doing it this way?
    from math import gcd

    return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this
# is simple enough:


def lcm(*numbers):
    """
    Return lowest common multiple of 1 or more integers.
    Examples
    --------
    >>> lcm(5)
    5
    >>> lcm(30, 40)
    120
    >>> lcm(120, 40, 60)
    120
    """
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, numbers, 1)

def create_moons(moon_text) -> List[Moon]:
    moons = []
    for moon in moons_text:
        parts = moon.strip('<>').split(',')
        t = []
        for i, part in enumerate(parts):
            dim, val = part.split('=')
            t.append(int(val))
        moons.append(Moon(*t))
    return moons



def run_sim(n, moons):
    for _ in range(n):
        for a in moons:
            for b in moons:
                if a != b:
                    a.calc_gravity(b)

        for moon in moons:
            moon.change_vel()
            moon.change_pos()

def part1():
    moons = create_moons(moons_text)
    run_sim(1000, moons)
    for moon in moons:
        print(moon)
        print(moon.calc_energy())


    print(sum([x.total_energy for x in moons]))

def part2():
    moons = create_moons(moons_text)
    counter = 0
    prev_state = False
    universe = {'x': set(), 'y': set(), 'z': set()}
    dimensions = ['x', 'y', 'z']
    dim_counts = {'x': 0, 'y': 0, 'z':0}
    while not prev_state:
        if counter % 10000 == 0:
            print(f'{counter} steps so far')
        curr_state = {'x': [], 'y': [], 'z': []}
        for moon in moons:
            curr_state['x'].append((moon.x_pos, moon.x_vel))
            curr_state['y'].append((moon.y_pos, moon.y_vel))
            curr_state['z'].append((moon.z_pos, moon.z_vel))

        for dim in dimensions:
            if dim_counts[dim] > 0:
                continue
            if tuple(curr_state[dim]) in universe[dim]:
                dim_counts[dim] = counter
                universe[dim].add(tuple(curr_state[dim]))
                print(f'{dim}: {counter} - {curr_state[dim]}')
            else:
                universe[dim].add(tuple(curr_state[dim]))
        if all(dim_counts.values()):
            break

        for a in moons:
            for b in moons:
                if a != b:
                    a.calc_gravity(b)
        for moon in moons:
            moon.change_vel()
            moon.change_pos()

        counter += 1

        # if counter == 0:
        #     universe.add(tuple(curr_state))

    print(dim_counts.values())
    # print(universe['x'][-1])
    counts = tuple(dim_counts.values())
    print(lcm(*counts))

part1()
part2()




