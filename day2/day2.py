with open('day2_input', 'r') as content_file:
    content = content_file.read()

input = list(map(lambda x: int(x), content.split(',')))

def run_program(program):
    i = 0
    current = program[i]
    while current != 99:
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        i += 4
        current = program[i]
    return program

print(run_program(input))
expected_result = 19690720
result = 0

for x in range(1, 100):
    for y in range(1, 100):
        input = list(map(lambda x: int(x), content.split(',')))
        input[1] = x
        input[2] = y
        if run_program(input)[0] == expected_result:
            print(x, y)
