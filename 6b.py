with open('6_input') as file:
    categories = file.read().split('\n')
times = categories[0].split()[1:]
time = ''
distances = categories[1].split()[1:]
distance = ''
for index in range(len(times)):
    time = time + times[index]
    distance = distance + distances[index]
timeInt = int(time)    
distanceInt = int(distance)
total = 1

for i in range(timeInt):
    if i * (timeInt-i) > distanceInt:
        total = total * (timeInt-2*i+1)
        break
print(total)