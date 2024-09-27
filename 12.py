import re

def checkGroup(input, groups):
    result = 0
    if groups == []:
        return 1
    size = groups[0]
    pattern = '[\.\?]'+size*"[\#\?]"+"[\.\?]"
    i = 0
    while i<len(input):
        # print(f"Level: {len(groups)} total: {result} size: {size} input: {input} position: {i}")
        match = re.search(pattern, input[i:])
        if match == None:
            return result
        begin, end = match.span()
        if "#" in input[begin:end] and len(groups) == 1:
            return result + 1
        nextInput = input[(i+end-1):]
        nextGroups = groups[1:]
        result += checkGroup(nextInput, nextGroups)
        i = i + begin + 1
    return result

with open('12_test_b') as file:
    lines = file.read().split('\n')

total = 0

for line in lines:
    input, groups = line.split()
    groups = [int(x) for x in groups.split(',')]
    input = '.'+input+'.'
    total += checkGroup(input, groups)
    print(total)
print(total)
