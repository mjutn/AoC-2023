with open('6_input') as file:
    categories = file.read().split('\n')
time = ''
time = time.join(categories[0].split()[1:])
distance = ''
distance = distance.join(categories[1].split()[1:])
timeInt = int(time)    
distanceInt = int(distance)
total = 1
for i in range(timeInt):
    if i * (timeInt-i) > distanceInt:
        total = total * (timeInt-2*i+1)
        break
print(total)