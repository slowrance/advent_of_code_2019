from math import floor

lines = []
with open('day01_data.txt') as f:
    lines = f.read().splitlines()

def calc_fuel(mass):
    fuel = floor(int(mass) / 3) - 2
    if fuel > 0:
        fuel += calc_fuel(fuel)
    else:
        fuel -= floor(int(mass) / 3) - 2
    print(f'mass: {mass}   fuel: {fuel}')
    return fuel

fuel = sum(map(calc_fuel, lines))

print(f'fuel required for modules: {fuel}')

