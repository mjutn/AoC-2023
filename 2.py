import re

with open('2_input') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    # make a dict to save values
    marbles = {'red': [], 'blue': [], 'green':[]}
    # prepare input
    line = re.split('; |: |, ', line)
    for index in range(1, len(line)):
        # only amount and colour seperated by a space in each list entry, so splitting gives amount and colour
        amount, colour = line[index].split()
        marbles[colour].append(int(amount))
    # check if legal amount of marbles used
    if max(marbles['red'])<13 and max(marbles['green'])<14 and max(marbles['blue'])<15:
        total += int(line[0].strip('Game:'))
# i gotta see my man
print(total)