import re
file = open('3_input')
lines = []
stars = {}
total = 0
for line in file:
    lines.append('.'+ line.strip('\n') + '.')
width = len(lines[0])
edge = '.' * width
lines.insert(0, edge)
lines.append(edge)
for i in range(1,len(lines)-1):
    for m in re.finditer('\d+', lines[i]):
        start, end = m.span()
        number = m.group()
        for j in range(i-1, i+2):
            for k in range(start-1, end+1):
                if lines[j][k] == '*':
                    if (j,k) not in stars:
                        stars[(j,k)] = [int(number)]
                    else:
                        stars[(j,k)].append(int(number))
for key in stars:
    if len(stars[key])==2:
        total += stars[key][0]*stars[key][1]
print(total)
file.close()