import re
from collections import Counter

def flip_lines(lines):
    flippedlines = ['']*len(lines[0])
    for index in range(len(lines)):
        for i in range(len(lines[index])):
            flippedlines[i] += lines[index][i]
    return flippedlines

with open('14_input') as file:
    lines = file.read().split('\n')

lines = flip_lines(lines)

total = 0
rank = len(lines[0])

for line in lines:
    matches = re.finditer('[^#]+', line)
    for m in matches:
        rocks = Counter(m.group())['O']
        for i in range(rocks):
            total += rank - m.start() - i
            
print(total)