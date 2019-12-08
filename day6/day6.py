with open('day6_input', 'r') as content_file:
    content = content_file.read()

input = list(map(lambda x: x.split(')'), content.split('\n')))


def assign_direct_orbits(input):
    orbits = {}
    for i in input:
        if i[0] not in orbits:
            orbits[i[0]] = [i[1]]
        else:
            orbits[i[0]] += [i[1]]
        if i[1] not in orbits:
            orbits[i[1]] = []
    return orbits


def count_all_orbits(orbits):
    count = 0
    for key, value in orbits.items():
        new = count_orbits_for_planet(orbits, value)
        count += new
    return count


def count_orbits_for_planet(orbits, planet):
    count = 0
    if not planet:
        return count
    for i in planet:
        count += 1 + count_orbits_for_planet(orbits, orbits[i])
    return count


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def calculate_shortest_path(input):
    path_to_you = list(dfs_paths(assign_direct_orbits(input), 'COM', 'YOU'))[0]
    path_to_santa = list(dfs_paths(assign_direct_orbits(input), 'COM', 'SAN'))[0]
    while len(path_to_santa) != 0:
        if path_to_you[0] == path_to_santa[0]:
            path_to_santa.pop(0)
            path_to_you.pop(0)
        else:
            return len(path_to_you) + len(path_to_santa) - 2


orbits = assign_direct_orbits(input)
print('Part 1 result: ' + str(count_all_orbits(orbits)))
print('Part 2 result: ' + str(calculate_shortest_path(input)))

