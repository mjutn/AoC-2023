import re

file = open('2_input')
colours = ['red', 'green', 'blue']
limit = [12, 13, 14]
total = 0
fault = False
for line in file:
    line = line.strip('\n')
    line = re.split('; |: |, | ', line)
    for i in range(len(line)):
        if i%2 != 0 or i == 0:
            continue
        elif int(line[i]) > limit[0] and line[i+1] == colours[0]:
            fault = True
        elif int(line[i]) > limit[1] and line[i+1] == colours[1]:
            fault = True
        elif int(line[i]) > limit[2] and line[i+1] == colours[2]:
            fault = True
    if fault is False:
        total += int(line[1])
    else:
        fault = False
print(total)