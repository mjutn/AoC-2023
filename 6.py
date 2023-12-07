with open('6_input') as file:
    categories = file.read().split('\n')
# get race time and records
times = [int(time) for time in categories[0].split()[1:]]
distances = [int(distance) for distance in categories[1].split()[1:]]
total = 1
# Find first hold length which gives a higher distance than record naively
# then the max hold length is the total time - first hold length, it is always symmetrical
# once answer has been found break the loop
for index in range(len(times)):
    for i in range(times[index]):
        if i * (times[index]-i) > distances[index]:
            total = total * (times[index]-2*i+1)
            break
# i gotta see my man
print(total)