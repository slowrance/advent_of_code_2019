
with open('day06_input.txt') as f:
    raw = f.read().splitlines()

d = {}
count = 0
for item in raw:
    parent, planet = item.split(')')
    d[planet] = parent

def count_orbits(planet):
    global count
    count += 1
    if d[planet] != 'COM':
        count_orbits(d[planet])

# part 1
for planet in d:
    count_orbits(planet)

print(count)


def get_orbits(planet, orbits):
    orbits.append(planet)
    if d[planet] != 'COM':
        get_orbits(d[planet], orbits)
    # return orbits

you_orbits = []
get_orbits(d['YOU'], you_orbits)
san_orbits = []
get_orbits(d['SAN'], san_orbits)

print(you_orbits)
print(san_orbits)

for i, you_orbit in enumerate(you_orbits):
    for j, san_orbit in enumerate(san_orbits):
        if you_orbit == san_orbit:
            print(you_orbit, i, j, i + j)
