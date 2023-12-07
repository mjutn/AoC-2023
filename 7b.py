from collections import Counter
file = open('7_input')
rankList = []
total = 0
encoding = [('A', 'E'), ('K','D'),('Q','C'),('J','1'),('T','A')]
for line in file:
    joker = 0
    line = line.split()
    for index in range(len(encoding)):
        line[0] = line[0].replace(encoding[index][0], encoding[index][1])
    charcount = Counter(line[0])
    if '1' in charcount.keys() and charcount['1'] != 5:
        joker = charcount['1']
        del charcount['1']
    most = max(charcount.values())
    different = len(charcount)
    score = int(line[0],16)+10000000*(most+joker-different)
    rankList.append((score,int(line[1])))
rankList.sort()
for i in range(len(rankList)):
    total += rankList[i][1] * (i+1)
print(total)