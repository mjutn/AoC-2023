import re
from math import lcm
with open('8_input') as file:
    lines = file.read().split('\n')
locations = {}
distances = []
for line in lines[2:]:
    line = re.split('\W+',line)
    locations[line[0]]=[line[1], line[2]]  
    ghosts = [loc for loc in locations if loc[2] == 'A']
    destinations = [loc for loc in locations if loc[2] == 'Z']
for ghost in ghosts:
    steps = 0
    while ghost not in destinations:
        for instruction in lines[0]:
            steps += 1
            if instruction == 'R':
                ghost = locations[ghost][1]
            elif instruction == 'L':
                ghost = locations[ghost][0]
            else:
                print('Something went wrong')
            if ghost in destinations:
                distances.append(steps)
                break
print(lcm(*distances))        