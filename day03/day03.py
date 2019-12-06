# part 1 correct answer is 768
l1 = []
l2 = []

with open('day03_input.txt') as f:
    lines = f.read().splitlines()
    l1, l2 = lines[0].split(','), lines[1].split(',')

# l1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
# l2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')


def move(current, direction, length):
    step_points = []
    new_pos = current

    if direction == 'U':
        for _ in range(length):
            new_pos = (new_pos[0], new_pos[1] + 1, new_pos[2] + 1)
            step_points.append(new_pos)
    elif direction == 'D':
        for _ in range(length):
            new_pos = (new_pos[0], new_pos[1] - 1, new_pos[2] + 1)
            step_points.append(new_pos)
    elif direction == 'L':
        for _ in range(length):
            new_pos = (new_pos[0] - 1, new_pos[1], new_pos[2] + 1)
            step_points.append(new_pos)
    elif direction == 'R':
        for _ in range(length):
            new_pos = (new_pos[0] + 1, new_pos[1], new_pos[2] + 1)
            step_points.append(new_pos)

    return new_pos, step_points




def get_points(line):
    points = []
    current_pos = (0, 0, 0)
    for step in line:
        new_pos, step_points = move(current_pos, step[0], int(step[1:]))
        points += step_points
        current_pos = new_pos


    return points


l1_points = get_points(l1)
l2_points = get_points(l2)
crosses = []
for point1 in l1_points:
    for point2 in l2_points:
        if point1[0] == point2[0] and point1[1] == point2[1]:
            print((point1, point2))
            crosses.append((point1, point2))

# crosses.sort(key=lambda x: abs(x[0] + abs(x[1])))

# for cross in crosses:
#     print(sum(cross[2]))

