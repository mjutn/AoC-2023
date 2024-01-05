with open('15_input') as file:
    input = file.read().split(',')

total = 0

for line in input:
    hash = 0
    for i in range(len(line)):
        hash = ((hash + ord(line[i]))*17)%256
    total += hash
print(total)