from math import atan2, pi
from operator import itemgetter

ast_map = '''
##.##..#.####...#.#.####
##.###..##.#######..##..
..######.###.#.##.######
.#######.####.##.#.###.#
..#...##.#.....#####..##
#..###.#...#..###.#..#..
###..#.##.####.#..##..##
.##.##....###.#..#....#.
########..#####..#######
##..#..##.#..##.#.#.#..#
##.#.##.######.#####....
###.##...#.##...#.######
###...##.####..##..#####
##.#...#.#.....######.##
.#...####..####.##...##.
#.#########..###..#.####
#.##..###.#.######.#####
##..##.##...####.#...##.
###...###.##.####.#.##..
####.#.....###..#.####.#
##.####..##.#.##..##.#.#
#####..#...####..##..#.#
.##.##.##...###.##...###
..###.########.#.###..#.'''.strip().split()

def calc_distance(origin, asteroid):
    return abs((asteroid[0] - origin[0]) + (asteroid[1] - origin[1]))

def get_targets(origin, asteroids):
    targets = []
    for ast in asteroids:
        if ast == origin:
            continue
        distance = calc_distance(origin, ast)
        target = (ast, calc_slope(origin, ast), distance)
        targets.append(target)

    return sorted(targets, key=itemgetter(1, 2))

def calc_slope(a, b):
    # try:
    radians = atan2(b[1] - a[1], b[0] - a[0])
    # except ZeroDivisionError:
    #     if a[1] > b[1]:
    #         return 'inf'
    #     else:
    #         return '-inf'
    # if slope == 0 and b[0] > a[0]:
    #     return str(slope)
    # elif slope == 0 and b[0] < a[0]:
    #     return str(slope)
    # else:
    #     return str(slope)
    return str((radians + (pi/2)) % (2 * pi))

def get_asteroids(ast_map):
    asteroids = []
    for i, row in enumerate(ast_map):
        for j, col in enumerate(row):
            if ast_map[i][j] =='#':
                asteroids.append((j, i))
    return asteroids

def count_detected(origin, asteroids):
    detected = set()
    for ast in asteroids:
        if ast == origin:
            continue
        # print(origin, calc_slope(origin, ast))
        detected.add(calc_slope(origin, ast))
    return origin, len(detected)

def destroy_targets(destroyed, targets):
    prev_target = (-1, -1, -1)
    remaining = []
    for target in targets:
        if prev_target[1] == target[1]:
            remaining.append(target)
            continue
        destroyed.append(target)
        print(target)
        prev_target = target
        # targets.remove(target)

    return destroyed, remaining

max_detected = 0
max_location = None
asteroids = get_asteroids(ast_map)
for ast in asteroids:
    detected = count_detected(ast, asteroids)
    if detected[1] > max_detected:
        max_detected = detected[1]
        max_location = detected[0]
print(max_detected, max_location)

for row in ast_map:
    print(row)


targets = get_targets((14, 17), asteroids)
print(targets)

destroyed = []
while len(destroyed) < 200:
    destroyed, targets = destroy_targets(destroyed, targets)
print(destroyed[199])





