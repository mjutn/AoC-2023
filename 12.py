import re

def checkGroup(input, groups):
    result = 0
    if groups == []:
        return 1
    size = groups[0]
    pattern = '[\.\?]'+size*"[\#\?]"+"[\.\?]"
    i = 0
    while i<len(input):
        match = re.search(pattern, input[i:])
        if match == None:
            break
        begin, end = match.span()
        result += checkGroup(input[(i+end-1):], groups[1:])
        i = i + begin + 1
    return result

with open('12_input') as file:
    lines = file.read().split('\n')

total = 0

for line in lines:
    input, groups = line.split()
    groups = [int(x) for x in groups.split(',')]
    input = '.'+input+'.'
    total += checkGroup(input, groups)
print(total)
