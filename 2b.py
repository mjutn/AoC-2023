import re

with open('2_input') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    marbles = {}
    minRed = minGreen = minBlue = 0
    line = re.split('; |: |, ', line)
    for index in range(1, len(line)):
        value, key = line[index].split()
        if key not in marbles.keys():
            marbles[key] = [int(value)]
        else:
            marbles[key].append(int(value))
    minRed = max(minRed, max(marbles['red']))
    minGreen = max(minGreen, max(marbles['green']))
    minBlue = max(minBlue, max(marbles['blue']))
    total += minRed * minGreen * minBlue
print(total)       