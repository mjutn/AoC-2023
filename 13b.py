def horizontal_reflection(lines):
    for point in range(len(lines)-1):
        smudge = (-1,-1)
        for i in range(len(lines)):
            if (point-i < 0 or point+1+i > len(lines)-1) and smudge != (-1,-1):
                return point
            elif point-i<0 or point+1+i > len(lines)-1:
                break
            for j in range(len(lines[0])):
                if lines[point-i][j] == lines[point+1+i][j]:
                    continue
                elif smudge == (-1,-1):
                    smudge = (point,i)
                else:
                    break
            else:
                continue
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
    if vpoint == -1 and hpoint == -1:
        for line in pattern:
            print(line)
        raise Exception("No match found")
print(total)