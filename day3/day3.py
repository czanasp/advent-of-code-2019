import math
import sys

with open('day3_input', 'r') as content_file:
    content = content_file.read()

input = list(map(lambda x: x.split(','), content.split('\n')))


test_case_1 = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']]
test_case_2 = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]
test_case_3 = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]



def create_paths(input):
    paths = [[], []]
    for i, path in enumerate(input):
        row = 0
        column = 0
        for direction in path:
            if direction[:1] == 'R':
                new_column = int(direction[1:])
                paths[i] += [(column+x, row) for x in range(0, new_column+1)]
                column += new_column
            if direction[:1] == 'L':
                new_column = int(direction[1:])
                paths[i] += [(column-x, row) for x in range(new_column, 0, -1)]
                column -= new_column
            if direction[:1] == 'U':
                new_row = int(direction[1:])
                paths[i] += [(column, row+x) for x in range(0, new_row+1)]
                row += new_row
            if direction[:1] == 'D':
                new_row = int(direction[1:])
                paths[i] += [(column, row-x) for x in range(new_row, 0, -1)]
                row -= new_row
    return paths


paths = create_paths(input)

print(len(paths[0]))
print(len(paths[1]))
same_points = []
shorter_path = paths[0] if len(paths[0]) <= len(paths[1]) else paths[1]
longer_path = paths[0] if len(paths[0]) > len(paths[1]) else paths[1]
best = sys.maxsize
for i, val in enumerate(shorter_path):
    print(i)
    if val != (0, 0) and val in longer_path:

        best = min(best, math.fabs(int(val[0]) + math.fabs(int(val[1]))))
        print(val)
        print('!!!!!!!!!!!!!!!!!! %s' % (best,))
print(same_points)

