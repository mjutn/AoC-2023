import re
file = open('3_input')
lines = []
total = 0
for line in file:
    lines.append('.'+ line.strip('\n') + '.')
width = len(lines[0])
edge = '.' * width
lines.insert(0, edge)
lines.append(edge)
nonSymbols = ['0','1','2','3','4','5','6','7','8','9','.']
for i in range(1,len(lines)-1):
    for m in re.finditer('\d+', lines[i]):
        start, end = m.span()
        number = m.group()
        for j in range(i-1, i+2):
            for k in range(start-1, end+1):
                if lines[j][k] not in nonSymbols:
                    total += int(number)
print(total)
file.close()