import re
with open('4_input') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    count = 0
    # get rid of text at start, and split the two halves into winning numbers and our numbers
    line = re.split(' \| |: ', line)
    winning = line[1].split()
    ours = line[2].split()
    # check for all our numbers if they are winning yes or no
    for number in ours:
        if number in winning:
            count += 1
    # if we won at least once, add it up to the score
    if count > 0:
        total += 2**(count-1)
# i gotta see my man
print(total)