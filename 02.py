import re
with open('2_input') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    marbles = {'red': [], 'blue': [], 'green':[]}
    line = re.split('; |: |, ', line)
    for index in range(1, len(line)):
        amount, colour = line[index].split()
        marbles[colour].append(int(amount))
    if max(marbles['red'])<13 and max(marbles['green'])<14 and max(marbles['blue'])<15:
        total += int(line[0].strip('Game:'))
print(total)