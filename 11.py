import re
import bisect
with open('11_input') as file:
    lines = file.read().split('\n')
emptyCols = []
emptyRows = []
galaxies = []
total = 0
for i in range(len(lines[0])):
    check = []
    for line in lines:
        check.append(line[i])
    if set(check) == {'.'}:
        emptyCols.append(i)
for i in range(len(lines)):
    if set(lines[i]) == {'.'}:
        emptyRows.append(i)
for i in range(len(lines)):
    rowOffset = bisect.bisect_left(emptyRows, i)
    hashes = re.finditer('#', lines[i])
    for m in hashes:
        index, _ = m.span()
        colOffset = bisect.bisect_left(emptyCols, index)
        galaxies.append((i+rowOffset, index+colOffset))
for i in range(len(galaxies)):
    startpoint = galaxies[i]
    for j in range(len(galaxies[i:])):
        endpoint = galaxies[i+j]
        total += abs(startpoint[0]-endpoint[0]) + abs(startpoint[1] - endpoint[1])
print(total)