from collections import defaultdict
class Encoding:
    def __init__(self):
        self.dest = defaultdict(list)
        self.src = defaultdict(list)
        self.rng = defaultdict(list)
    def append(self, key, ints):
        if self.src[key] == []:
            self.src[key].append(ints[1])
            self.dest[key].append(ints[0])
            self.rng[key].append(ints[2])
        else:
            for index in range(len(self.src[key])+1):
                if index == len(self.src[key]):
                    self.dest[key].append(ints[0])
                    self.src[key].append(ints[1])
                    self.rng[key].append(ints[2])
                    break
                if self.src[key][index] <= ints[1]:
                    continue
                elif self.src[key][index] > ints[1]:
                    self.dest[key].insert(index, ints[0])
                    self.src[key].insert(index, ints[1])
                    self.rng[key].insert(index, ints[2])
                    break

with open('5_input') as f:
    sections = f.read().split('\n\n')
keys = ['seed', 'soil', 'fert', 'water', 'light', 'temp', 'humid']
enc = Encoding()
for index in range(1,len(sections)):
    lines = sections[index].split('\n')
    for line in lines:
        line = line.split()
        if not line[0].isdigit():
            continue
        else:
            ints = list(map(int, line))
            enc.append(keys[index-1], ints)

inputRanges = sections[0].split()[1:]
inputRanges = list(map(int, inputRanges))
best = 2147483647
for i in range(10):
    print(i)
    source = inputRanges[2*i]
    fullRange = inputRanges[2*i+1]
    seed = source
    while seed < source + fullRange:
        loc = seed
        skip = source+fullRange-loc
        for key in keys:
            for index in range(len(enc.src[key])):
                src = enc.src[key][index]
                rng = enc.rng[key][index]-1
                dest = enc.dest[key][index]
                if loc > src + rng:
                    if index == len(enc.src[key])-1:
                        break
                    continue    
                elif src <= loc <= src + rng:
                    loc = dest-src+loc
                    skip = min(skip, src + rng - loc)
                    break
                elif loc < src:
                    skip = min(skip, src-loc)
                    break
                else:
                    print('something is going wrong')
            
        best = min(best, loc)
        if skip > 0:
            seed = seed + skip
        else:
            seed = seed + 1
print(best)