import Image

with open('day8_input', 'r') as content_file:
    content = content_file.read()

input = [int(d) for d in str(content)]

print(input)


def find_the_layer(input):
    zeros_count = 151
    starting_index = -1
    for i in range(0, len(input), 150):
        if zeros_count > input[i:i+150].count(0):
            zeros_count = min(zeros_count, input[i:i+150].count(0))
            starting_index = i
    return input[starting_index:starting_index+150]


def build_image(input):
    image = [2]*150
    for i in range(0, 150):
        for j in range(i, len(input), 150):
            if input[j] != 2:
                image[i] = input[j]
                break
    return image


layer = find_the_layer(input)
print(layer)
print('Part 1 result: ' + str(layer.count(1) * layer.count(2)))
print('Part 2 result: ' + ''.join(map(str, build_image(input))))




value = ''.join(map(str, build_image(input)))

cmap = {'0': (255,255,255),
        '1': (0,0,0)}

data = [cmap[letter] for letter in value]
img = Image.new('RGB', (8, len(value)//8), "white")
img.putdata(data)
img.show()
