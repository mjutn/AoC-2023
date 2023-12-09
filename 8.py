import re
with open('8_input') as file:
    lines = file.read().split('\n')
locations = {}
for line in lines[2:]:
    line = re.split('\W+',line)
    locations[line[0]]=[line[1], line[2]]    
location = 'AAA'
steps = 0
while location != 'ZZZ':
    for instruction in lines[0]:
        steps += 1
        if instruction == 'R':
            location = locations[location][1]
        elif instruction == 'L':
            location = locations[location][0]
        else:
            print('Something went wrong')
        if location == 'ZZZ':
            break
print(steps)
        