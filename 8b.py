import re
from math import lcm
with open('8_input') as file:
    lines = file.read().split('\n')
distances = []
ghosts = [re.split('\W+',s)[0] for s in lines[2:] if s[2] == 'A']
destinations = [re.split('\W+',s)[0] for s in lines[2:] if s[2] == 'Z']
for ghost in ghosts:
    steps = 0
    while ghost not in destinations:
        for instruction in lines[0]:
            steps += 1
            nodes = [re.split('\W+',line) for line in lines if line.startswith(ghost)][0]
            if instruction == 'R':
                ghost = nodes[2]
            elif instruction == 'L':
                ghost = nodes[1]
            else:
                print('Something went wrong')
            if ghost in destinations:
                distances.append(steps)
                break
print(lcm(*distances))        