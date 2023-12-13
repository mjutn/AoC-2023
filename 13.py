def horizontal_reflection(lines):
    for point in range(len(lines)-1):
        for i in range(len(lines)):
            if point-i < 0 or point+1+i > len(lines)-1:
                return point
            if lines[point-i] == lines[point+1+i]:
                continue
            else:
                break
    return -1
        
def flip_lines(lines):
    flippedlines = ['']*len(lines[0])
    for index in range(len(lines)):
        for i in range(len(lines[index])):
            flippedlines[i] += lines[index][i]
    return flippedlines

with open('13_input') as file:
    patterns = file.read().split('\n\n')

total = 0

for pattern in patterns:
    pattern = pattern.split('\n')
    flippedlines = flip_lines(pattern)
    hpoint = horizontal_reflection(pattern)
    if hpoint > -1:
        total += (hpoint+1)*100
        continue
    vpoint = horizontal_reflection(flippedlines)
    if vpoint > -1:
        total += vpoint+1
print(total)