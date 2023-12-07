from collections import defaultdict
# I put all mappings into one class. The key corresponds to a map, and the integers are the numbers.
# destination, source, range.
# I sort by source, so that it is easier to see where the input compares to the mapping.
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
                if self.src[key][index] >= ints[1]:
                    continue
                elif self.src[key][index] < ints[1]:
                    self.dest[key].insert(index, ints[0])
                    self.src[key].insert(index, ints[1])
                    self.rng[key].insert(index, ints[2])
                    break

with open('5_input') as f:
    sections = f.read().split('\n\n')
enc = Encoding()
for index in range(1,len(sections)):
    lines = sections[index].split('\n')
    for line in lines:
        line = line.split()
        # ignore the lines without useful information
        if not line[0].isdigit():
            continue
        else:
            # put the maps into my data structure
            ints = list(map(int, line))
            enc.append(index, ints)
low = 99999999999
# first line is the seeds we take through the mapping
seeds = [int(seed) for seed in sections[0].split()[1:]]
for seed in seeds:
    for key in enc.src:
        for index in range(len(enc.src[key])):
            # verify if the seed is within the range, or higher than the highest
            # range - 1 as it includes the src itself as a number.
            src = enc.src[key][index]
            rng = enc.rng[key][index]-1
            dest = enc.dest[key][index]
            if seed > src + rng:
                break
            if src <= seed <= src + rng:
                seed = dest-src+seed
                break 
    low = min(low, seed)
# i gotta see my man
print(low)