from collections import namedtuple
from typing import List

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

moons = create_moons(moons_text)

def run_sim(n):
    for _ in range(n):
        for a in moons:
            for b in moons:
                if a != b:
                    a.calc_gravity(b)

        for moon in moons:
            moon.change_vel()
            moon.change_pos()

def part1():
    run_sim(1000)
    for moon in moons:
        print(moon)
        print(moon.calc_energy())


    print(sum([x.total_energy for x in moons]))

def part2():
    counter = 0
    prev_state = False
    universe = {}
    while not prev_state:
        if counter % 100000 == 0:
            print(f'{counter} steps tried so far')
        curr_state = []
        for a in moons:
            for b in moons:
                if a != b:
                    a.calc_gravity(b)
        for moon in moons:
            moon.change_vel()
            moon.change_pos()
            curr_state.append(moon.curr_state())
        if tuple(curr_state) in universe:
            print(f'returned to previous state after {counter} steps')
            break
        if counter == 0:
            universe.add(tuple(curr_state))
        counter += 1
part1()
part2()




