import re
with open('4_input') as file:
    lines = file.read().split('\n')
total = 0
copies = [1]*len(lines)
for index in range(len(lines)):
    count = 0
    line = re.split(' \| |: ', lines[index])
    winning = line[1].split()
    ours = line[2].split()
    for number in ours:
        if number in winning:
            count += 1
    for i in range(1, count+1):
        copies[index+i] += copies[index]
print(sum(copies))