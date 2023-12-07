import re
# read input
with open('2_input') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    # make dict to save values
    marbles = {'red':[],'green':[],'blue':[]}
    # split line into chunks of colour and amount
    line = re.split('; |: |, ', line)
    for index in range(1, len(line)):
        # split into amount and colour
        amount, colour = line[index].split()
        marbles[colour].append(int(amount))
    # get minimum of marbles needed so no illegal moves are happening
    minRed = max(marbles['red'])
    minGreen = max(marbles['green'])
    minBlue = max(marbles['blue'])
    # add it up
    total += minRed * minGreen * minBlue
# i gotta see my man
print(total)       