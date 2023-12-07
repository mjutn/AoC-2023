with open('6_input') as file:
    categories = file.read().split('\n')
# cat input to strings to make one large number, then make it an int
time = ''
time = time.join(categories[0].split()[1:])
distance = ''
distance = distance.join(categories[1].split()[1:])
timeInt = int(time)    
distanceInt = int(distance)
total = 1
# find first number naively, second number is symmetrical. Break loop once answer been found
# there are better ways to do this, but this is fast enough don't judge me
for i in range(timeInt):
    if i * (timeInt-i) > distanceInt:
        total = total * (timeInt-2*i+1)
        break
# i gotta see my man
print(total)