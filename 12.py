import re

with open('12_test') as file:
    lines = file.read().split('\n')

total = 0

for line in lines:
    input, groups = line.split()
    print(input +"|"+ groups+"\n")
    groups = [int(x) for x in groups if x.isdigit()]
    hashtagsTotal = sum(groups)
    minLength = hashtagsTotal + len(groups) -1
    dotsAdded = len(input)-minLength

    if dotsAdded == 0:
        total += 1
        continue
    
    unknownGroups = re.split('\.', input)
    unknownGroups = list(filter(None, unknownGroups))
    print(unknownGroups)