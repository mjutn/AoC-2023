import re
with open('2_input') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    marbles = {'red':[],'green':[],'blue':[]}
    line = re.split('; |: |, ', line)
    for index in range(1, len(line)):
        amount, colour = line[index].split()
        marbles[colour].append(int(amount))
    minRed = max(marbles['red'])
    minGreen = max(marbles['green'])
    minBlue = max(marbles['blue'])
    total += minRed * minGreen * minBlue
print(total)       