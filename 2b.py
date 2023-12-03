import re

file = open('2_input')
colours = ['red', 'green', 'blue']
limit = [12, 13, 14]
total = 0
minRed = 0
minBlue = 0
minGreen = 0
fault = False
for line in file:
    line = line.strip('\n')
    line = re.split('; |: |, | ', line)
    for i in range(len(line)):
        if i%2 != 0 or i == 0:
            continue
        elif line[i+1] == colours[0]:
            if int(line[i]) > minRed:
                minRed = int(line[i])
        elif line[i+1] == colours[1]:
            if int(line[i]) > minGreen:
                minGreen = int(line[i])
        elif line[i+1] == colours[2]:
            if int(line[i]) > minBlue:
                minBlue = int(line[i])
    total += minRed * minGreen * minBlue
    minRed = 0
    minBlue = 0
    minGreen = 0
print(total)