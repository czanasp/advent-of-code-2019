with open('day3_input', 'r') as content_file:
    content = content_file.read()

input = list(map(lambda x: x.split(','), content.split('\n')))


test_case_1 = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']]



def create_paths(input):
    paths = [[], []]
    row = 0
    column = 0
    for i, path in enumerate(input):
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


print(create_paths(test_case_1))
a = [['.']*1000]*1000
for i, path in enumerate(create_paths(test_case_1)):
    for spot in path:
        a[500+spot[0]][500+spot[1]] = '*'

print('\n'.join(map(''.join, a)))
# mapa = [['.']*]