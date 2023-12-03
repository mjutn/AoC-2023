import re

file = open('3_input')
lines = []
above = []
below = []
total = 0
schematic = False
for line in file:
    lines.append(line)
for i in range(len(lines)):
    current = lines[i]
    list = [m.span() for m in re.finditer('\d+', current)]
    matches = [m.group() for m in re.finditer('\d+', current)]
    for j in range(len(list)):
        a, b = list[j]
        if (current[a-1] != '.' and a > 0)or (current[b] != '.' and b < len(current)-1):
            schematic = True
        if i == 0:
            below = lines[i+1]
            for k in range(a-1, b+1):
                if k < len(current)-1 and k >= 0 and below[k] != '.':
                    schematic = True
        elif i == len(lines)-1:
            above = lines[i-1]
            for k in range(a-1, b+1):
                if k < len(current) and above[k] != '.':
                    schematic = True
        else:
            above = lines[i-1]
            below = lines[i+1]
            for k in range(a-1, b+1):
                if k < len(current)-1 and k >= 0 and (above[k] != '.' or below[k] != '.'):
                    schematic = True
        if schematic == True:
            total += int(matches[j])
            schematic = False
print(total)