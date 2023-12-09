import re
with open('8_input') as file:
    lines = file.read().split('\n')
location = 'AAA'
steps = 0
while location != 'ZZZ':
    for instruction in lines[0]:
        steps += 1
        nodes = [re.split('\W+',line) for line in lines if line.startswith(location)][0]
        if instruction == 'R':
            location = nodes[2]
        elif instruction == 'L':
            location = nodes[1]
        else:
            print('Something went wrong')
        if location == 'ZZZ':
            break
print(steps)
        