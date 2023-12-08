import re
with open('8_input') as file:
    lines = file.read().split('\n')
location = 'AAA'
steps = 0
while location != 'ZZZ':
    for instruction in lines[0]:
        if location == 'ZZZ':
            break
        steps += 1
        nodes = [i for i in lines if i.startswith(location)]
        locations = re.split('\W+', nodes[0])
        if instruction == 'R':
            location = locations[2]
        elif instruction == 'L':
            location = locations[1]
        else:
            print('Something went wrong')
print(steps)
        