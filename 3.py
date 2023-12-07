import re

file = open('3_input')
lines = []
total = 0
# in order to get rid of annoying edge cases, 
# append a . before and after string, 
# and insert line of dots above and below
for line in file:
    lines.append('.'+ line.strip('\n') + '.')
width = len(lines[0])
edge = '.' * width
lines.insert(0, edge)
lines.append(edge)
# All things we don't consider a symbol in a list
nonSymbols = ['0','1','2','3','4','5','6','7','8','9','.']
for i in range(1,len(lines)-1):
    # find number (not digit) in line, save number and remember indices
    for m in re.finditer('\d+', lines[i]):
        start, end = m.span()
        number = m.group()
        # check line above, line itself and line below for symbols
        for j in range(i-1, i+2):
            for k in range(start-1, end+1):
                if lines[j][k] not in nonSymbols:
                    total += int(number)
# i gotta see my man
print(total)
file.close()