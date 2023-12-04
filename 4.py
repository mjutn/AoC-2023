import re
with open('4_input') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    count = 0
    line = re.split(' \| |: ', line)
    winning = line[1].split()
    ours = line[2].split()
    for i in ours:
        if i in winning:
            count += 1
    if count > 0:
        total += 2**(count-1)
print(total)