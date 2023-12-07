import re
with open('4_input') as file:
    lines = file.read().split('\n')
total = 0
# I make a list, so I can remember how many copies of each card I have
copies = [1]*len(lines)
for index in range(len(lines)):
    count = 0
    # split the line into a list with our numbers and a list with winning numbers
    line = re.split(' \| |: ', lines[index])
    winning = line[1].split()
    ours = line[2].split()
    # find the amount of winning numbers
    for number in ours:
        if number in winning:
            count += 1
    # now we gotta copy for the amount of copies that we have
    for i in range(1, count+1):
        copies[index+i] += copies[index]
# i gotta see my man
print(sum(copies))