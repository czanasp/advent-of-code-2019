with open('day1_input', 'r') as content_file:
    content = content_file.read()

input = list(map(lambda x: int(x), content.split('\n')))


def fuel_required_to_launch(mass):
    fuel_needed = (mass//3)-2
    if fuel_needed < 0:
        return 0
    return fuel_needed + fuel_required_to_launch(fuel_needed)


def fuel_requirement(input):
    result = 0
    for i in input:
        result += fuel_required_to_launch(i)
    return result


print(fuel_requirement(input))