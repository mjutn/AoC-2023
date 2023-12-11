from collections import Counter
file = open('7_input')
rankList = []
total = 0
encoding = [('A', 'E'), ('K','D'),('Q','C'),('J','B'),('T','A')]
for line in file:
    line = line.split()
    for index in range(len(encoding)):
        line[0] = line[0].replace(encoding[index][0], encoding[index][1])
    most = max(Counter(line[0]).values())
    different = len(Counter(line[0]))
    score = int(line[0],16)+10000000*(most-different)
    rankList.append((score,int(line[1])))
rankList.sort()
for i in range(len(rankList)):
    total += rankList[i][1] * (i+1)
print(total)
file.close()