class Encoding:
    def __init__(self):
        self.dest = []
        self.src = []
        self.rng = []
    def append(self, ints):
        self.dest.append(ints[0])
        self.src.append(ints[1])
        self.rng.append(ints[2])
    def reset(self):
        self.dest = []
        self.src = []
        self.rng = []

def findDest(seed, enc):
    for index in range(len(enc.dest)):
        if enc.src[index] <= seed <= enc.src[index]+enc.rng[index]:
            return enc.dest[index] + seed - enc.src[index]
        else:
            if index == len(enc.dest)-1:
                return seed
            continue

file = open('5_test')
seeds = file.readline().split()[1:]
seeds = list(map(int, seeds))
enc = Encoding()
file.readline()

for line in file:
    if not line.strip():
        break
    line = line.split()
    if not line[0].isdigit():
        continue
    else:
        ints = list(map(int, line))
        enc.append(ints)
for i in range(len(seeds)):
    seeds[i] = findDest(seeds[i], enc)
enc.reset()

print(seeds)