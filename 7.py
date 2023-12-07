from collections import Counter
file = open('7_input')
rankList = []
total = 0
# change input to decimal numbers, so conversion to int gives correct order
encoding = [('A', 'E'), ('K','D'),('Q','C'),('J','B'),('T','A')]
for line in file:
    line = line.split()
    # change all the characters to the ones I want
    for index in range(len(encoding)):
        line[0] = line[0].replace(encoding[index][0], encoding[index][1])
    # find most common character
    most = max(Counter(line[0]).values())
    # find amount of unique characters (to distinguish between three of a kind and full house for example)
    different = len(Counter(line[0]))
    # score is the hex number plus offset for the different types of hands. Save score and bid as a tuple
    score = int(line[0],16)+10000000*(most-different)
    rankList.append((score,int(line[1])))
# sorting the score also sorts the bids (tuple) so that's nice
rankList.sort()
# go through the list and multiply bid by index + 1
for i in range(len(rankList)):
    total += rankList[i][1] * (i+1)
# i gotta see my man
print(total)
file.close()