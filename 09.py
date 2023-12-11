with open('9_input') as file:
    lines = file.read().split('\n')
lineEnds = []
for line in lines:
    old = [int(i) for i in line.split()]
    final = [old[-1]]
    while set(old) != {0} and len(old)>1:
        new = []
        for index in range(len(old)-1):
            new.append(old[index+1]-old[index])
        old = new
        final.append(old[-1])
    for index in range(len(final)-2, -1, -1):
        final[index] = final[index]+final[index+1]
    lineEnds.append(final[0])
print(sum(lineEnds))