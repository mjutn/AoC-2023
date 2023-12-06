with open('6_input') as file:
    categories = file.read().split('\n')
times = [int(time) for time in categories[0].split()[1:]]
distances = [int(distance) for distance in categories[1].split()[1:]]
total = 1
for index in range(len(times)):
    for i in range(times[index]):
        if i * (times[index]-i) > distances[index]:
            total = total * (times[index]-2*i+1)
            break
print(total)