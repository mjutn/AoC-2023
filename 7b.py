from collections import Counter
file = open('7_input')
rankList = []
total = 0
# change numbers into hexadecimal, lucky me the one is still free to make joker least high
encoding = [('A', 'E'), ('K','D'),('Q','C'),('J','1'),('T','A')]
for line in file:
    joker = 0
    line = line.split()
    # encode all characters which should be encoded
    for index in range(len(encoding)):
        line[0] = line[0].replace(encoding[index][0], encoding[index][1])
    # this time save the counter object, a dict with character as key and occurance as value
    charcount = Counter(line[0])
    # if the joker is in the hand we save the amount of jokers and then delete the entry
    # as any hand with jokers except 5 jokers is essentially a hand with more of a different number
    # entry is deleted so unique character and most common character calculation works
    if '1' in charcount.keys() and charcount['1'] != 5:
        joker = charcount['1']
        del charcount['1']
    most = max(charcount.values())
    different = len(charcount)
    # offset for type, add amount of jokers to most common character
    score = int(line[0],16)+10000000*(most+joker-different)
    rankList.append((score,int(line[1])))
rankList.sort()
# yes
for i in range(len(rankList)):
    total += rankList[i][1] * (i+1)
# i gotta see my man
print(total)
file.close()