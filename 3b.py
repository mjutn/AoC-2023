import re

file = open('3_input')
lines = []
# I'm using a dict, with the coordinates of a star as key.
# this means that multiple numbers corresponding to the same star end up in one list.
stars = {}
total = 0
# remove edge cases by adding dots above, below, to the left and right of the actual input
for line in file:
    lines.append('.'+ line.strip('\n') + '.')
width = len(lines[0])
edge = '.' * width
lines.insert(0, edge)
lines.append(edge)
for i in range(1,len(lines)-1):
    # first find numbers
    for m in re.finditer('\d+', lines[i]):
        start, end = m.span()
        number = m.group()
        # then check around the number to see if there is a star.
        # if so, add dict entry for that specific star
        for j in range(i-1, i+2):
            for k in range(start-1, end+1):
                if lines[j][k] == '*':
                    if (j,k) not in stars:
                        stars[(j,k)] = [int(number)]
                    else:
                        stars[(j,k)].append(int(number))
# now take each star, see if there's two numbers and if so, multiply those numbers
for key in stars:
    if len(stars[key])==2:
        total += stars[key][0]*stars[key][1]
# i gotta see my man
print(total)
file.close()